import sys
import cv2
import numpy as np
sys.path.append('..')
from miniCG import img, poly, transform, window
import time

# Image shape
h = 500
w = 500

# Viewport and Window 01
v1 = np.array([0, 0, h/2-1, w/2-1], np.float32)
j1 = np.array([-1, -1, 1, 1], np.float32)

# Viewport and Window 02
v2 = np.array([0, w/2-1, h-1, w-1], np.float32)
j2 = np.array([1, 1, 10, 10], np.float32)

# Load texture
tex = cv2.imread("../assets/cat.jpg")
tex = cv2.cvtColor(tex, cv2.COLOR_RGB2GRAY)

# Load texture
bike1 = cv2.imread("../assets/bike1.png")
bike1 = cv2.cvtColor(bike1, cv2.COLOR_RGB2GRAY)

# Load bike1ture
bike2 = cv2.imread("../assets/bike2.png")
bike2 = cv2.cvtColor(bike2, cv2.COLOR_RGB2GRAY)

# Create Polygon 01
p1 = poly.create()
p1 = poly.insert_dot(p1, [-0.5, -0.5, 0, 0])
p1 = poly.insert_dot(p1, [0.5, -0.5, 1, 0])
p1 = poly.insert_dot(p1, [0.5, 0.5, 1, 1])
p1 = poly.insert_dot(p1, [-0.5, 0.5, 0, 1])

# Create Polygon 02
p2 = poly.create()
p2 = poly.insert_dot(p2, [7, 7, 0, 0])
p2 = poly.insert_dot(p2, [9, 7, 1, 0])
p2 = poly.insert_dot(p2, [9, 9, 1, 1])
p2 = poly.insert_dot(p2, [7, 9, 0, 1])


# Create Polygon 02
p3 = poly.create()
p3 = poly.insert_dot(p2, [15, 20, 0, 0])
p3 = poly.insert_dot(p2, [32, 45, 1, 0])
p3 = poly.insert_dot(p2, [12, 32, 1, 1])
p3 = poly.insert_dot(p2, [32, 54, 0, 1])

circle_points = poly.draw_circle(70, 400, 17)

# Create transformation matrix: Rotation
m_t = transform.create()
m_t = transform.rotation(m_t, 2)

m_t_b = transform.create()
m_t_b = transform.translation(m_t_b, -1, 0)

# Animation loop
# Press Esc to end animation
k = None
bike = bike1
while(k != 27):
    # Create clean image
    m = img.create(w, h)
    
    for point in circle_points:
         m = img.set_pixel(m, point[1], point[0], 100, 100, 100)
    
    # Nova cor para preenchimento
    new_color = (255, 255, 255)

    # Aplica o preenchimento com o algoritmo de Flood Fill
    m = img.flood_fill(m, (70, 400), 220, 200, 200)
    
    # Map Poly 01 to Viewport 01
    pv = window.map_multi(p1, j1, v1)

    # pvc = window.map_multi(circle_points, j1, v1)
    # Do Scanline
    m = img.scan_line(m, pv, tex)
    # Map Poly 02 to Viewport 01
    pv = window.map_multi(p2, j1, v1)
    # Do Scanline
    m = img.scan_line(m, pv, tex)
    # Map Poly 01 to Viewport 02
    pv = window.map_multi(p1, j2, v2)
    # Do Scanline
    m = img.scan_line(m, pv, bike1)
    # Map Poly 02 to Viewport 02
    pv = window.map_multi(p2, j2, v2)
    # Do Scanline
    m = img.scan_line(m, pv, bike1)
    # Show image generated
    cv2.imshow("Test", m)
    # Apply transformation: Rotation
    p1 = transform.apply(p1, m_t)
    p2 = transform.apply(p2, m_t_b)
    # Wait 10 milsecs or capture key pressed
    k = cv2.waitKey(10)
    time.sleep(2)