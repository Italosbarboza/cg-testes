import sys
import cv2
import numpy as np
sys.path.append('..')
from miniCG import img, poly, transform, window
import time

def opening():
    k = None
    # Image shape
    h = 500
    w = 500
    
    while(k != 27):
        abertura = img.create(w, h)
        cv2.imshow("Test", abertura)
        k = cv2.waitKey(10)
