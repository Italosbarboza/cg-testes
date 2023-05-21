import sys
import cv2
import numpy as np
sys.path.append('..')
from miniCG import img, poly, transform, window
import time

def animation(): 

    # Image shape
    h = 500
    w = 500
     
    # Viewport and Window 01
    v1 = np.array([0, 0, w, h/2], np.float32)
    j1 = np.array([1, 1, 10, 10], np.float32)
    
    # Viewport and Window 02
    v2 = np.array([0, h/2 + 1, w - 1, h - 1], np.float32)
    j2 = np.array([1, 1, 10, 10], np.float32)
    
    # Load texture
    tex = cv2.imread("../assets/cat.jpg")
    
    # Load texture
    bike1 = cv2.imread("../assets/bike1.png")
    
    # Load bike1ture
    bike2 = cv2.imread("../assets/bike2.png")
    
    # Create Polygon 01
    p1 = poly.create()
    p1 = poly.insert_dot(p1, [1, 1, 0, 0])
    p1 = poly.insert_dot(p1, [10, 1, 1, 0])
    p1 = poly.insert_dot(p1, [10, 10, 1, 1])
    p1 = poly.insert_dot(p1, [1, 10, 0, 1])
    
    # Create Polygon 02
    p2 = poly.create()
    p2 = poly.insert_dot(p2, [7, 7, 0, 0])
    p2 = poly.insert_dot(p2, [9, 7, 1, 0])
    p2 = poly.insert_dot(p2, [9, 9, 1, 1])
    p2 = poly.insert_dot(p2, [7, 9, 0, 1])
    
    
    p_sol = poly.draw_circulo(40, 440, 20)
    
    # Create transformation matrix: Rotation
    m_t = transform.create()
    m_t = transform.rotation(m_t, 2)
    
    m_t_b = transform.create()
    m_t_b = transform.translation(m_t_b, -1, 0)
    
    # Animation loop
    # Press Esc to end animation
    k = None
    bike = bike1
    control = 0
    while(k != 27):
        # Create clean image
        m = img.create(w, h)
        
        # Map Poly 02 to Viewport 01
        pv = window.map_multi(p1, j1, v1)
        # pv2 = window.map_multi(p_sol, j1, v1)
        # Do Scanline
        m = img.scan_line(m, pv, tex)
    
        # Map Poly 02 to Viewport 02
        pv = window.map_multi(p2, j2, v2)
        # Do Scanline
        m = img.scan_line(m, pv, bike)
    
        m = poly.set_circulo(m, p_sol, 244, 158, 18)
        # Show image generated
        cv2.imshow("Test", m)
        # Apply transformation: Rotation
        # p1 = transform.apply(p1, m_t)
        p2 = transform.apply(p2, m_t_b)
        # Wait 10 milsecs or capture key pressed
        k = cv2.waitKey(10)
        time.sleep(2)
    
        if (control == 0):
            bike = bike2
            control = control + 1
        else:
            bike = bike1
            control = 0