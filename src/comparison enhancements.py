import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('ip images/slide1.jpg',0) #load images
#apply various in-built OpenCV thresholding functions to the image
ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)
titles = ['Greyscaling','Binary thresholding','Inverse binary thresholding','Truncate thresholding','Thresholding to zero','Inverse thresholding to zero']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
#iteratively plot the images
for i in range(6):
    plt.figure(figsize = (30,30))
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

#ret, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

imginv = (255-img) #digital negative of original image
equ = cv2.equalizeHist(img) #histogram equaliation
equinv = (255-equ)#digital negative of equalized image

plt.figure(figsize = (10,10))
plt.imshow(equ,'gray',vmin=0,vmax=255) 
plt.title('Histogram equalization')
plt.show()

plt.figure(figsize = (10,10))
plt.imshow(equinv,'gray',vmin=0,vmax=255)
plt.title('Inverted histogram equalization')
plt.xticks([]),plt.yticks([])
plt.show()

plt.figure(figsize = (10,10))
plt.imshow(imginv,'gray',vmin=0,vmax=255)
plt.title('Inverted greyscale image')
plt.xticks([]),plt.yticks([])
plt.show()

img = cv2.imread('slide1.jpg',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) #create a contrast limited adaptive histograme (CLAHE) function
cl1 = clahe.apply(img)
plt.figure(figsize = (10,10))
plt.imshow(cl1,'gray',vmin=0,vmax=255)
plt.title('CLAHE (Contrast Limited Adaptive Histogram Equalization)')
plt.xticks([]),plt.yticks([])
plt.show()

cl2 = (255-cl1) #digital negative of CLAHE image
plt.figure(figsize = (10,10))
plt.imshow(cl2,'gray',vmin=0,vmax=255)
plt.title('Inverted CLAHE')
plt.xticks([]),plt.yticks([])
plt.show()
