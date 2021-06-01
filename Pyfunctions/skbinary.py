"""
Created on Thu Apr  1 2021

@author: alexf
"""
    
import numpy as np
import matplotlib.pyplot as plt #plt for displaying the images

def skbinary(blurarray, user_thres):
    """
    skbinary converts images to binary using manual thresholding, first run "skblur" on an image, select your threshold value, which should be <1.0,
    and then run the function. Before running, declare an empty array called "binaryempty" (see skblur docstring).

    Parameters
    ----------
    blurarray: array 
        blurred image array to be processed.
    user_thres: int/float 
        threshold set for the binary thresholding
    
    Returns
    -------
    binary_image: array
        binary image array
    """
    
    threshold = user_thres
    
    binary_image =  np.array(blurarray > threshold, dtype=int) #if value is less than threshold, it is set to black
    
    fig, axes = plt.subplots(ncols=3, figsize=(12,5))
    ax = axes.ravel()

    ax[0].imshow(blurarray, cmap=plt.cm.gray)
    ax[0].set_title('input blurred image')

    ax[1].hist(blurarray.ravel(), bins=256)
    ax[1].set_title('Histogram with chosen threshold')
    ax[1].axvline(threshold, color='r')

    ax[2].imshow(binary_image, cmap=plt.cm.gray)
    ax[2].set_title('binary - manual filter')
      
    return(binary_image)