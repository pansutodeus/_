from PIL import Image
from PIL.PngImagePlugin import PngInfo

import math
import numpy as np
import random

def sf(im, seed=666):
    # Get pixels and put in Numpy array for easy shuffling
    pix = np.array(im.getdata())

    # Generate an array of shuffled indices
    # Seed random number generation to ensure same result
    np.random.seed(seed)
    indices = np.random.permutation(len(pix))

    # Shuffle the pixels and recreate image
    shuffled = pix[indices].astype(np.uint8)
 
    return Image.fromarray(shuffled.reshape(im.width,im.height,3))

def uf(im, seed=666):

    # Get shuffled pixels in Numpy array
    shuffled = np.array(im.getdata())
    nPix = len(shuffled)

    # Generate unshuffler
    np.random.seed(seed)
    indices = np.random.permutation(nPix)
    unshuffler = np.zeros(nPix, np.uint32)
    unshuffler[indices] = np.arange(nPix)

    unshuffledPix = shuffled[unshuffler].astype(np.uint8)
    return Image.fromarray(unshuffledPix.reshape(im.width,im.height,3))

def genInfo(pnginfo):
    pnginfo = PngInfo()
    for k, v in INFO.items():
        pnginfo.add_text(k, str(v))

    return pnginfo