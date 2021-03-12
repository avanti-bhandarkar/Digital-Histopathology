import cv2

showCrosshair = False #Set crosshair parameter of the cv2.selectROI to false - selection rectangle will not have a crosshair
fromCenter = False #Set default centering parameter of the cv2.selectROI to false - selected image will not be centered at initial mouse position

# Select region of interest from the loaded image
print('Select a region with no nuclei in it and press enter/return to save it')
img = cv2.imread("ip images/pathology_slide_5.PNG") #Load image
roi_nonu = cv2.selectROI(img, fromCenter, showCrosshair) #Run the default CV2 ROI function
# Crop image to match seleted ROI
nonucleus_region = img[int(roi_nonu[1]):int(roi_nonu[1]+roi_nonu[3]), int(roi_nonu[0]):int(roi_nonu[0]+roi_nonu[2])] #Select region between the top left and bottom right corner of the rectangle and crop it
# Display cropped image
cv2.imshow('Region with no nuclei',nonucleus_region)
cv2.imwrite('op images/nonucleus_region.png',nonucleus_region) #Save the cropped image
cv2.waitKey(0) # Waits for user indefinitely to click enter key and exit external GUI windows
