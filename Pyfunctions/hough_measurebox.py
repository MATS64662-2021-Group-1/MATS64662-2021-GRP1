# -*- coding: utf-8 -*-
"""
Created on Fri May 14 2021

@author: alexf
"""

from skimage import measure
from skimage.transform import hough_line, hough_line_peaks
from scipy import ndimage

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def hough_measurebox(bin_array, background, min_line_dist, min_line_angle, fraction, peak_no):
    """
    hough_meaurebox is a function that performs a hough transform of the given array (or binary image) which has been sliced
    according to labelled image regions from skimage label and ndimage. This was based on the previous function hough_measure and 
    code by M. Maric (HAPPy).\nHough lines are plotted for each object detected from the hough peaks onto the input image in rectangles which are generated
    from the object size. \nBefore using, ensure your array is binary (dtype=int). The image will be labelled into regions
    according to skimage.measure.label, for this you choose background type. Connectivity is defined as the number of dimensions
    equal to that in the original image.
    
    Parameters
    ----------
    
    bin_array: array 
        Binary image
    
    background: int 
        background = 1 is recommended and defines white as the image background.
        
    min_line_dist: int 
        The minimum distance which separates detected hough lines (int). Approximately 5 is reccomended.
        
    min_line_angle: int 
        The minimum angle separating lines (int). Approximately 5 seems acceptable, 
        but depending on the hydride formation you may want to increase it, 
        e.g. 20 will eliminate illogical diagonal connectivity paths.
        
    fraction: float
        This filter value specifies the minimum intensity of hough peaks (hydride dimension), 
        by default this is 0.5*max(hspace) from houghspace_array. A value of 0.3 is recommended. 0.5 may be too large, 
        and this will elimate lines that are less than 50% of the size of the "largest" line detected.
            
    peak_no: int 
        The maximum number of peaks that should be detected by the hough_line_peaks from skimage. Reccommended
        5, increase if you need to increase the number of detected hydrides.
        
    Returns
    -------
    angles, heights: array
        column 0: angles (deg), column 1: heights (pixels)
        
    """

    #label image region using skimage.label, connectivity = dimension of the image
    #scipy is then used to slice the array around objects
    imlabels, num_labels = measure.label(bin_array, background=background, return_num=True, connectivity=bin_array.ndim)
    imslices = ndimage.find_objects(imlabels)
    
    #define test angle range, -pi/2 to pi/2 is the default and is acceptable
    test_angles = np.linspace(-np.pi/2, np.pi/2, 90)
    
    #declare plots
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    ax = axes.ravel()

    #plot 1 - display input image
    ax[0].imshow(bin_array, cmap=plt.cm.gray) 
    ax[0].set_title('Input binary image')
    ax[0].set_axis_off()
    
    #plot 2 - display original image and detected objects with hough lines
    ax[1].imshow(bin_array, cmap=plt.cm.gray)
    ax[1].set_title('Detected objects or hydrides')
    ax[1].set_ylim((bin_array.shape[0], 0))
    ax[1].set_xlim((0, bin_array.shape[1]))
    ax[1].set_axis_off()
    
    #define hough parameter lists
    angle_list  = []
    height_list = [] 
    
    #perform hough line transform, looped through each object slice
    for object in np.arange(num_labels):
        houghspace_array, theta, distances = hough_line(
            imlabels[imslices[object]], 
            theta=test_angles)
        
        #threshold is equal to the fraction*max(hspace), changed from default
        hough_thres = fraction*np.amax(houghspace_array) 
    
        #Read the hough line peaks for the object, taking specified inputs
        h_peak, angle, dist_peak = hough_line_peaks(
            houghspace_array, 
            theta, 
            distances,
            min_distance = min_line_dist, 
            min_angle = min_line_angle, 
            threshold = hough_thres,
            num_peaks = peak_no)
        
        #append peak parameters to lists
        height_list.append(h_peak)
        angle_list.append(angle)
        
        #draw rectangle around the sliced objects
        x0_rect = np.min([imslices[object][1].stop, imslices[object][1].start])
        x1_rect = np.max([imslices[object][1].stop, imslices[object][1].start])
        
        y0_rect = np.min([imslices[object][0].stop, imslices[object][0].start])
        y1_rect = np.max([imslices[object][0].stop, imslices[object][0].start])
       
        #rectangle of origin (x0,y0), width = (x1-x0) and height (y1-y0)
        rectangle = Rectangle((x0_rect, y0_rect),
                              (x1_rect - x0_rect),
                              (y1_rect - y0_rect),
                              angle = 0,
                              edgecolor = 'b',
                              fill = False)
        
        ax[1].add_patch(rectangle)

        #find hough line peaks and plot straight lines
        #origin is the top left of the box, point 0 and width of box
        origin = np.array((0, x1_rect - x0_rect))
    
        for h, a, d in zip(h_peak, angle, dist_peak):
            ya, yb = (d - origin * np.cos(a)) / np.sin(a)

            y0_line = ya + y0_rect
            y1_line = yb + y0_rect

            x0_line = x0_rect
            x1_line = x1_rect

            #if the line origin < box starting point, then line width is set to the box widths
            if y0_line < y0_rect:
                y0_line = y0_rect

            if y1_line < y0_rect:
                y1_line = y0_rect

            if y0_line > y1_rect:
                y0_line = y1_rect   

            if y1_line > y1_rect:
                y1_line = y1_rect      

            ax[1].plot((x0_line, x1_line), (y0_line, y1_line), 'r')
   
    plt.show()
    
    #convert angles to degrees
    degangles = [x*180/np.pi for x in angle_list]
    
    #as each iteration produces its own list, they must be concatenated
    heights = np.concatenate(height_list)
    angles = np.concatenate(degangles) 
    
    #a 2 column array of [angles, heights] is then returned
    return(np.column_stack((angles , heights )))