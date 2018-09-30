# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 21:46:03 2018

@author: nilsh
"""

import random
from PIL import Image, ImageFilter


def _and(a,b):
    return a&b

def _or(a,b):
    return a|b

def _xor(a,b):
    return a^b

def encoder(im, pix, seed, operator=_xor):
#    im = Image.open(imagePath)
#    pix = im.load()
    width, height = im.size
    
    random.seed(seed)
    
    for i in range(height):
        for j in range(width):
            pix[j,i] = operator(pix[j,i],random.randint(0,255))
        
    return im
    

#im = Image.open("files/Babbage.jpg")
#
#pix = im.load()
#
#
#width, height = im.size

#rgb_im = im.convert("RGB")

#pix[10,10] = 12
#
#print(pix[10,10])

#print(rgb_im[0,1])

#for i in range(height):
#    for j in range(width):
#        #rgb_im.getpixel((width,height)) = (0,0,0)
#        pix[j,i] = pix[j,i] ^ 150

#im.save("files/newImage.jpg")
im = Image.open("files/Babbage.jpg") 
pix = im.load()

encoder(im, pix, 150, _xor)

#im.show()

encoder(im, pix, 150, _xor)

im.show()
        
#a = 244
#b = 135
#
#c = a^b
#
#print(c)



#print(im.size)
#print(rgb_im.getpixel((0,1)))

