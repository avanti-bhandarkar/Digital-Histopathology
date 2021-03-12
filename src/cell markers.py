#import required libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import feature
import scipy.ndimage as ndi
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from PIL import Image
from helpers import detect_peaks


prob = cv2.imread('probability map.jpg') #load generated probability map
img = cv2.imread('slide1.jpg') #load original image
prob = cv2.cvtColor(prob, cv2.COLOR_BGR2GRAY) #convert probability map from rgb to grayscale
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) #create a contrast limited histogram equalization function
prob = clahe.apply(prob) #apply clahe to the image
ret,thresh = cv2.threshold(prob,100,255,cv2.THRESH_BINARY) #apply binary thresholding to the equalized image
gauss = cv2.GaussianBlur(thresh,(15,15),0) #apply a gaussian blurring filter to the thresholded image such that the arguments are (sigmaX,sigmaY), 0 = constant interpolation of border pixels
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15)) #define an elliptical kernel or structural element
opening = cv2.morphologyEx(gauss,cv2.MORPH_OPEN,kernel, iterations = 2) #perform morphological opening on the filtered image over 2 iterations using the elliptical kernel
