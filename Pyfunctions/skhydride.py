"""
Created on Thu Apr  1 2021

@author: alexf
"""
from skimage import filters 
from skimage.color import rgb2gray #Import necessary skimage modules; for reading images, filtering and converting to grayscale

import matplotlib.pyplot as plt #plt for displaying the images
import numpy as np

def skblur(imarray, user_1, user_2):
    
    """
    skblur uses scikit image to apply greyscale to an .jpg image and then 
    apply a Gaussian blur, based on specficied inputs. First run "jpg_list" 
    function to provide a convenient list of jpp files to input, the specify 
    arguments. 
    
    After the function has run, it will save an image of size equal to your 
    original image called "blurred_image_YOURFILENAME." 

    Parameters
    ----------
    imarray: array
        image array
    user_1: float
        sigma value for Gaussian blur, reccommended 0<x<1
    user_2: float
        gaussian truncation value, truncates the filter after this many 
        standard deviations 
        
    Returns
    -------
    blurarray: array
        blurred image array
    
    """
   
  
    try:
        
        user_sigma = float(user_1)
        user_trunc = float(user_2) #functions inputs are converted to floats, as they are dtype=str
        
        
        grayscale_image = rgb2gray(imarray) #image is converted to greyscale (note: this creates a float value array)
    
        blurred_image = filters.gaussian(grayscale_image, sigma=user_sigma, truncate=user_trunc) #skimage gaussian filter with specified input
        #Default parameters: (image, sigma=1, output=None, mode='nearest', cval=0, multichannel=None, preserve_range=False, truncate=4.0)
        
        
        #figure1 states that matplotlib will plot the 3 images in comparison; the original, greyscale and then the gaussian blur
        #it is necessary to specify cmap=plt.cm.gray, otherwise greyscale will be displayed in green/purple,
        #and binary will be displayed as a binary heatmap.
        
        fig1, axes = plt.subplots(ncols=3, figsize=(15,5))
        ax = axes.ravel()

        ax[0].imshow(imarray)
        ax[0].set_title('Original image')
        
        ax[1].imshow(grayscale_image, cmap=plt.cm.gray)
        ax[1].set_title('Greyscale')
        
        ax[2].imshow(blurred_image, cmap=plt.cm.gray)
        ax[2].set_title('Gaussian blur')
        
        blurarray=blurred_image[:,:]
               
        return(blurarray)        
        
#Exception handling, incase of file, input or value errors    
    except FileNotFoundError as e:
        print("File not found, check paths \n" , e)
    except IOError as e:
        print("Input error\n" , e)
    except ValueError as e:
        print("Value input error, check what you have input: \n",e)
        
        
def skbinary(blurarray, user_thres):
    """
    skbinary converts images to binary using manual thresholding, first run 
    "skblur" on an image, select your threshold value, which should be <1.0, 
    and then run the function.

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