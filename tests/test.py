import sys
import cv2
import numpy as np
sys.path.append('..')
from miniCG import img, poly, transform, window
import time

def set_pixel(img, x, y, r, g, b):
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    
    if x > img.shape[1]-1:
        x = img.shape[1]-1
    if y > img.shape[0]-1:
        y = img.shape[0]-1
    
    x, y = int(round(x)), int(round(y))

    img[y, x] = (b, g, r)

    return img

def flood_fill(image, start_pixel, new_color):
    rows, cols, _ = image.shape
    original_color = image[start_pixel[0], start_pixel[1]]
    
    # Verifica se a cor inicial é igual à nova cor
    if np.array_equal(original_color, new_color):
        return image
    
    # Função auxiliar para verificar se uma posição está dentro dos limites da imagem
    def is_valid_position(row, col):
        print(rows)
        return 0 <= row < rows and 0 <= col < cols
    
    # Função recursiva para preencher a área
    def fill(row, col):
        if not is_valid_position(row, col) or not np.array_equal(image[row, col], original_color):
            return

        # Pinta o pixel com a nova cor
        image[row, col] = new_color
        
        # Chama a função recursivamente para os vizinhos
        fill(row - 1, col)  # Vizinho superior
        fill(row + 1, col)  # Vizinho inferior
        fill(row, col - 1)  # Vizinho esquerdo
        fill(row, col + 1)  # Vizinho direito
    
    
    # Chama a função de preenchimento
    fill(start_pixel[0], start_pixel[1])
    
    return image

def create(w, h):
    return np.zeros((h, w, 3), np.uint8)

# Image shape
h = 300
w = 300

# Viewport and Window 01
v1 = np.array([0, 0, h/2-1, w/2-1], np.float32)
j1 = np.array([-1, -1, 1, 1], np.float32)

# Viewport and Window 02

v2 = np.array([0, w/2-1, h-1, w-1], np.float32)
j2 = np.array([1, 1, 10, 10], np.float32)
# Load texture
tex = cv2.imread("../assets/cat.jpg")
tex = cv2.cvtColor(tex, cv2.COLOR_RGB2BGR)

# Load texture
bike1 = cv2.imread("../assets/bike1.png")
bike1 = cv2.cvtColor(bike1, cv2.COLOR_RGB2BGR)

# Load bike1ture
bike2 = cv2.imread("../assets/bike2.png")
bike2 = cv2.cvtColor(bike2, cv2.COLOR_RGB2BGR)

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


circle_points = poly.draw_circle(70, 200, 17)

# Create transformation matrix: Rotation
m_t = transform.create()
m_t = transform.rotation(m_t, 2)

m_t_b = transform.create()
m_t_b = transform.translation(m_t_b, -1, 0)

# Animation loop
# Press Esc to end animation
k = None
bike = bike1

# Cria uma imagem preta de 300x300
image = create(300, 300)

# Define as coordenadas do pixel
x = 150
y = 150

# Define as cores RGB do gradiente
start_color = (255, 0, 0)  # Vermelho
end_color = (0, 0, 255)    # Azul

# Calcula a diferença de cores para cada canal (R, G, B)
color_diff = tuple((end - start) // 299 for start, end in zip(start_color, end_color))

# Preenche a imagem com o gradiente de cores
for i in range(300):
    r = start_color[0] + color_diff[0] * i
    g = start_color[1] + color_diff[1] * i
    b = start_color[2] + color_diff[2] * i

    set_pixel(image, i, y, r, g, b)

for point in circle_points:
         image = set_pixel(image, point[1], point[0], 100, 100, 100)

new_color = np.array([255, 255, 255], dtype=np.uint8)

image = img.flood_fill(image, (70, 200), new_color)
    

# Exibe a imagem na tela usando o OpenCV
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
