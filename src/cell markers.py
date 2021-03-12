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


prob = cv2.imread('op images/probability map.jpg') #load generated probability map
img = cv2.imread('ip images/slide1.jpg') #load original image

prob = cv2.cvtColor(prob, cv2.COLOR_BGR2GRAY) #convert probability map from rgb to grayscale
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) #create a contrast limited histogram equalization function
prob = clahe.apply(prob) #apply clahe to the image
ret,thresh = cv2.threshold(prob,100,255,cv2.THRESH_BINARY) #apply binary thresholding to the equalized image

gauss = cv2.GaussianBlur(thresh,(15,15),0) #apply a gaussian blurring filter to the thresholded image such that the arguments are (sigmaX,sigmaY), 0 = constant interpolation of border pixels
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15)) #define an elliptical kernel or structural element
opening = cv2.morphologyEx(gauss,cv2.MORPH_OPEN,kernel, iterations = 2) #perform morphological opening on the filtered image over 2 iterations using the elliptical kernel

markers = detect_peaks(opening) #generate nuclei markers by using the defined helper function detect_peaks to find local maxima values

#save the nuclei markers (generated as a numpy array) into an image
im = Image.fromarray(markers)
im.save('markers.jpg')

cell_markers = cv2.imread('op images/markers.jpg')
cell_markers = cv2.erode(cell_markers, None, iterations = 9) #apply erosion operation on the markers to optain point markers for the nuclei

#save the obtained numpy array of point markers as an image
im = Image.fromarray(cell_markers)
im.save('op images/cell_markers.jpg') 

cell_markers = Image.open(r'op images/cell_markers.jpg').convert('L') 
slide = Image.open(r'ip images/slide1.jpg')
mask = Image.open(r'op images/cell_markers.jpg').convert('L') 

#create a composite image consisting of the both the images and a transparent mask formed from the point markers image
composite = Image.composite(cell_markers,slide,mask) 
composite = composite.save("op images/composite.jpg") #save the composite image
