import cv2
import PIL.Image, colorsys    
import pandas as pd
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

img = Image.open("1.jpg")
m,n = img.size

#RGB colourspace
imgrgb = img.copy()
RGB = list(imgrgb.getdata())
df_RGB = pd.DataFrame(RGB, columns = ['R','G','B'])

df_RGB.to_csv('RGB.csv', index=False)

#HSV colourspace
def HSVColor(img):
    if isinstance(img,Image.Image):
        r,g,b = img.split()
        Hdat = []
        Sdat = []
        Vdat = [] 
        for rd,gn,bl in zip(r.getdata(),g.getdata(),b.getdata()) :
            h,s,v = colorsys.rgb_to_hsv(rd/255.,gn/255.,bl/255.)
            Hdat.append(int(h*255.))
            Sdat.append(int(s*255.))
            Vdat.append(int(v*255.))
        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)
        return Image.merge('RGB',(r,g,b))
    else:
        return None

imghsv = Image.open('1.jpg')
imghsv_final = HSVColor(imghsv)
HSV = list(imghsv_final.getdata())

df_HSV = pd.DataFrame(HSV, columns = ['H','S','V'])
df_HSV.to_csv('HSV.csv', index=False)

#LAB colourspace
img = cv2.imread('1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_RGB2Lab)
cv2.imwrite('imglab.jpg',img)
imglab_final = Image.open("imglab.jpg")
LAB = list(imglab_final.getdata())

df_LAB = pd.DataFrame(LAB, columns = ['L','A','B'])
df_LAB.to_csv('LAB.csv', index=False)
