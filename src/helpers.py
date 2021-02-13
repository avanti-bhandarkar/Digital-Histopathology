#Import lbraries
from PIL import Image

#Define a function to convert RGB (Red, Blue, Green) to HSV (Hue, Saturation, Value) colourspace 
def rgb_to_hsv(r, g, b):
    maxc = max(r, g, b) # Extract maximum red,blue and green values from the image
    minc = min(r, g, b) # Extract minimum red,blue and green values from the image
    v = maxc # Set value equal to maximum RGB value
    if minc == maxc: # If maximum and minimum values are equal, set hue and saturation value to 0
        return 0.0, 0.0, v
    s = (maxc-minc) / maxc # Set saturation value to the ratio rgb range and maximum rgb value
    # Initialise red, blue and green channels in terms of maximum/minimum values and inputs to the function
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    # Define hue values using an else-if ladder as per the formulae used here (https://www.rapidtables.com/convert/color/rgb-to-hsv.html)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, s, v

#Define a function to obtain HSV color from the loaded image
def HSVColor(img):
    if isinstance(img,Image.Image): # The code below is only executed if the image has been loaded using PIL
        r,g,b = img.split() # Split the RGB image into constituent channels
        # Initialise empty lists for HSV values
        Hdat = [] 
        Sdat = []
        Vdat = [] 
        for rd,gn,bl in zip(r.getdata(),g.getdata(),b.getdata()) : # Get pixel values for rgb channels from the images and zip them
            h,s,v = rgb_to_hsv(rd/255.,gn/255.,bl/255.) # Apply previouslty defined rgb_to_hsv function and append the values obtained into the blank lists
            Hdat.append(int(h*255.))
            Sdat.append(int(s*255.))
            Vdat.append(int(v*255.))
        # Copy HSV values pixelwise to form 3 channels
        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)
        # Merge the 3 channels obtained in the previous step to get a complete HSV image
        return Image.merge('RGB',(r,g,b))
    else:
        return None
