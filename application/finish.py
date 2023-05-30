import sys
import cv2
import numpy as np
sys.path.append('..')
from miniCG import img, poly, transform, window
import time

def finish(): 

    # Image shape
    h = 600
    w = 800

   # Window
    j = np.array([-1, -1, 2, 1], np.float32)

    # Load texture
    tex = cv2.imread("../assets/pokebola.png")

    # Create Polygon 01
    p1 = poly.create()
    p1 = poly.insert_dot(p1, [-0.5, -0.5, 0, 0])
    p1 = poly.insert_dot(p1, [0.5, -0.5, 1, 0])
    p1 = poly.insert_dot(p1, [0.5, 0.5, 1, 1])
    p1 = poly.insert_dot(p1, [-0.5, 0.5, 0, 1])

    # Create transformation matrix: Rotation
    m_t = transform.create()
    m_t = transform.rotation(m_t, 2)

    # Animation loop
    # Press Esc to end animation
    k = None
    while(k != 27):
        # Create clean image
        m = img.create(w, h)

        # Map Poly 01 to Viewport
        pv1 = window.map(p1, j, [w, h])
        # Do Scanline
        m = img.scan_line(m, pv1, tex)

        # Show image generated
        cv2.imshow("Test", m)
        # Apply transformation: Rotation
        p1 = transform.apply(p1, m_t)

        time.sleep(2) 

        # Wait 10 milsecs or capture key pressed
        k = cv2.waitKey(10)