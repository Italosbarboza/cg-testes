import sys
import cv2
import numpy as np
sys.path.append('..')
from primitiveFunctions import img, poly, transform, window
import time

def finish(): 

    # Image shape
    h = 600
    w = 800

   # Window
    j = np.array([1, 1, 30, 30], np.float32)

    # Load texture
    pikashu = cv2.imread("../assets/pikashu.png")
    pikashu = cv2.cvtColor(pikashu, cv2.COLOR_BGR2RGB)

    pokebola = cv2.imread("../assets/pokebola.png")
    pokebola = cv2.cvtColor(pokebola, cv2.COLOR_BGR2RGB)


    # Create Polygon 01
    p1 = poly.create()
    p1 = poly.insert_dot(p1, [12, 12, 0, 0])
    p1 = poly.insert_dot(p1, [16, 12, 1, 0])
    p1 = poly.insert_dot(p1, [16, 16, 1, 1])
    p1 = poly.insert_dot(p1, [12, 16, 0, 1])

    # Create Polygon 01
    p2 = poly.create()
    p2 = poly.insert_dot(p2, [4, 4, 0, 0])
    p2 = poly.insert_dot(p2, [6, 4, 1, 0])
    p2 = poly.insert_dot(p2, [6, 6, 1, 1])
    p2 = poly.insert_dot(p2, [4, 6, 0, 1])

    # Create Polygon 03
    p3 = poly.create()
    p3 = poly.insert_dot(p3, [24, 24, 0, 0])
    p3 = poly.insert_dot(p3, [26, 24, 1, 0])
    p3 = poly.insert_dot(p3, [26, 26, 1, 1])
    p3 = poly.insert_dot(p3, [24, 26, 0, 1])


    # Create transformation matrix: Rotation
    m_t = transform.create()
    m_t = transform.translation(m_t, -14, -14)
    m_t = transform.scale(m_t, 1.3, 1.3)
    m_t = transform.translation(m_t, 14, 14)

    m_r = transform.create()
    m_r = transform.translation(m_r, -5, -5)
    m_r = transform.rotation(m_r, 5)
    m_r = transform.translation(m_r, 5, 5)

    m_r2 = transform.create()
    m_r2 = transform.translation(m_r2, -25, -25)
    m_r2 = transform.rotation(m_r2, 5)
    m_r2 = transform.translation(m_r2, 25, 25)

    # Animation loop
    # Press Esc to end animation
    k = None
    count = 0
    while(k != 27):
        # Create clean image
        m = img.create(w, h)

        # Map Poly 01 to Viewport
        pv1 = window.map(p1, j, [w, h])
        pv2 = window.map(p2, j, [w, h])
        pv3 = window.map(p3, j, [w, h])

        # Do Scanline
        m = img.scan_line(m, pv1, pikashu)
        m = img.scan_line(m, pv2, pokebola)
        m = img.scan_line(m, pv3, pokebola)


        # Show image generated
        cv2.imshow("Animation", m)
        # Apply transformation: Rotation
        p1 = transform.apply(p1, m_t)
        p2 = transform.apply(p2, m_r)
        p3 = transform.apply(p3, m_r2)

        time.sleep(2) 

        count = count + 1

        # Wait 10 milsecs or capture key pressed
        k = cv2.waitKey(10)