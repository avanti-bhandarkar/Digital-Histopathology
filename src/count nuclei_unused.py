#import libraries
import imageio
from scipy import ndimage

# load image
opened = imageio.imread('opened.jpg')

# smooth the image using Gaussian filter with sigma = 1 (to remove small objects in the background)

filtered = ndimage.gaussian_filter(opened, 1)
T = 75 # set size threshold manually
       
# find connected components 
labeled, number = ndimage.label(filtered > T) #only give the image components with pixel size greater than T value
#labeled gives an integer array where each unique feature in the input has a unique label in the returned array
#number gives the number of components (nuclei) detected in the image based on the threshold limit
print ("Number of nuclei in the image is %d " % number)

# show labeled image

import matplotlib.pyplot as plt
plt.figure(figsize=(20,20))
plt.imsave('labeled.jpg', labeled)
plt.imshow(labeled,cmap='gray',vmax=255,vmin=0)
plt.show()
