# -*- coding: utf-8 -*-
"""
Created on Wed May 12 2021

@author: alexf
"""
import numpy as np

def RHF_prop(hough_measure_array):
 
    """This functions calculates the proportion of radial hydrides by assessing 
    each angle by the criteria created by (Colas, 2013). However, it is 
    modified for use with hough_measure.py, as angles are taken in respect 
    to the y-axis using this function as opposed to in respect to the 
    circumferential direction.
    
    
     Parameters
    ----------
    hough_measure_array: array 
        the output of the hough_measure function, angles and heights.
        
    Returns
    -------
    rhf: float
        radial hydride fraction
    max: int/float
        maximum hydride size detected in pixels
    min: int/float
        maximum hydride size detected in pixels
           
    """
    
    #produce a list of absolute angles by slicing column 1 from the input array from hough_measure
    angles = [abs(x) for x in hough_measure_array[:,0]]
    sizes = hough_measure_array[:,1]
    
    #maximum and minimum hydride sizes
    max = np.max(sizes)
    min = np.min(sizes)
    
    #define an empty list where weighting will be added
    weightings = []
    
    for y in angles:
        if 0 < y <= 40:
            f = 1
        
        elif 40 < y <=65:
            f = 0.5
            
        elif 65 < y <=90:
            f = 0
        
        #append to list
        weightings.append(f)
    
       
    fi = np.array(weightings)

    #take the multiplication of each weighting and size
    #lenfi = fi * sizes
        
    rhf = sum(fi * sizes)/sum(sizes)
    
    #a 2 decimal place round is implemented, to allow quick assessment of RHF
    rhf2 = round(rhf, 2)
    
    return(rhf2, max, min)
    
           