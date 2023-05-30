import sys
import cv2
import numpy as np
sys.path.append('..')
from primitiveFunctions import img, poly, transform, window, clipping
import time
# bgr
def animation(): 

    # Image shape
    h = 600
    w = 800
     
    # Viewport and Window 01
    v1 = np.array([0, 0, w, h/2], np.float32)
    j1 = np.array([1, 1, 10, 10], np.float32)
    
    # Viewport and Window 02
    v2 = np.array([0, h/2 + 1, w - 1, h - 1], np.float32)
    j2 = np.array([1, 1, 10, 10], np.float32)
    
    tex = cv2.imread("../assets/ceu.jpg")
    tex = cv2.cvtColor(tex, cv2.COLOR_BGR2RGB)

    ground = cv2.imread("../assets/ground.png")
    ground = cv2.cvtColor(ground, cv2.COLOR_BGR2RGB)

    bike1 = cv2.imread("../assets/bike1.png")
    bike1 = cv2.cvtColor(bike1, cv2.COLOR_BGR2RGB)
    
    bike2 = cv2.imread("../assets/bike2.png")
    bike2 = cv2.cvtColor(bike2, cv2.COLOR_BGR2RGB)

    press = cv2.imread("../assets/esc.png")
    press = cv2.cvtColor(press, cv2.COLOR_BGR2RGB)
    
    # Create Polygon 01
    p1 = poly.create()
    p1 = poly.insert_dot(p1, [1, 1, 0, 0])
    p1 = poly.insert_dot(p1, [10, 1, 1, 0])
    p1 = poly.insert_dot(p1, [10, 10, 1, 1])
    p1 = poly.insert_dot(p1, [1, 10, 0, 1])
    
    # Create Polygon 02
    p2 = poly.create()
    p2 = poly.insert_dot(p2, [7, 3, 0, 0])
    p2 = poly.insert_dot(p2, [9, 3, 1, 0])
    p2 = poly.insert_dot(p2, [9, 5, 1, 1])
    p2 = poly.insert_dot(p2, [7, 5, 0, 1])

    # Create Polygon 02
    ptt = poly.create()
    ptt = poly.insert_dot(ptt, [1, 5, 0, 0])
    ptt = poly.insert_dot(ptt, [10, 5, 1, 0])
    ptt = poly.insert_dot(ptt, [10, 10, 1, 1])
    ptt = poly.insert_dot(ptt, [1, 10, 0, 1])

    # Create Polygon 02
    p3 = poly.create()
    p3 = poly.insert_dot(p3, [7, 8, 0, 1])
    p3 = poly.insert_dot(p3, [9, 8, 1, 1])
    p3 = poly.insert_dot(p3, [9, 6, 1, 0])
    p3 = poly.insert_dot(p3, [7, 6, 0, 0])
    
    p_sol = poly.draw_circulo(40, 440, 20)
    
    
    m_t_b = transform.create()
    m_t_b = transform.translation(m_t_b, -1, 0)
    
    # Animation loop
    # Press Esc to end animation
    k = None
    bike = bike1
    control = 0
    control2 = 0
    while(k != 27):
        m = img.create(w, h)
        
        pv = window.map_multi(p1, j1, v1)

        m = img.scan_line(m, pv, tex)
    
        pv = window.map_multi(p2, j2, v2)
        pvt = window.map_multi(ptt, j2, v2)

        m = img.scan_line(m, pv, bike)
        m = img.scan_line(m, pvt, ground)

        pv = window.map_multi(p3, j2, v2)

        pv = clipping.apply(v2, pv)

        control2 = control2 + 1
        
        if (control2 >= 6):
            # Do Scanline
            m = img.scan_line(m, pv, press)
    
        m = poly.set_circulo(m, p_sol, 244, 158, 18)

        m = poly.fill_circle(m, 440, 40, 20, (255, 192, 0), (255, 192, 0))

        m = img.scan_line(m, ptt, press)


        cv2.imshow("Animation", m)

        p2 = transform.apply(p2, m_t_b)
        
        k = cv2.waitKey(10)
        time.sleep(2)
    
        if (control == 0):
            bike = bike2
            control = control + 1
        else:
            bike = bike1
            control = 0