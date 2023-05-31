import numpy as np
import cv2
import sys
sys.path.append('..')
from primitiveFunctions import img, poly
import time

def opening():
    # Dimensões da imagem
    width = 800
    height = 600

    # Tamanho desejado para a imagem aumentada
    new_width = 600
    new_height = 400

    # Cria a imagem
    image = img.create(width, height)

    # Coordenadas da primeira reta (acima)
    x1 = 0
    y1 = 50
    x2 = 0
    y2 = 50
    intensity = (255, 0, 0)  # Cor em RGB (vermelho)

    # Coordenadas da segunda reta (abaixo)
    x3 = width - 1
    y3 = 755
    x4 = width - 1
    y4 = 755
    intensity2 = (0, 0, 255)  # Cor em RGB (azul)

    # Cria os círculos
    circle1_center_x = x1 + 20  # Posição à esquerda da reta vermelha
    circle1_center_y = height/256  # Posição vertical central da tela
    circle1_radius = 15

    circle2_center_x = x3 - 225  # Posição à direita da reta azul
    circle2_center_y = height *1.5  # Posição vertical central da tela
    circle2_radius = 15

    # Criação das elipses
    ellipse1_center_x = width - 225  # Posição à direita da reta vermelha
    ellipse1_center_y = height - 511 # Posição vertical superior
    ellipse1_radius_x = 20
    ellipse1_radius_y = 30

    ellipse2_center_x = 21  # Posição à esquerda da reta azul
    ellipse2_center_y = height + 113  # Posição vertical inferior
    ellipse2_radius_x = 20
    ellipse2_radius_y = 30

    # Create Polygon 01
    p1 = poly.create()
    p1 = poly.insert_dot(p1, [width // 2 - new_width // 2, height // 2 - new_height // 2, 0, 0])
    p1 = poly.insert_dot(p1, [width // 2 + new_width // 2, height // 2 - new_height // 2, 1, 0])
    p1 = poly.insert_dot(p1, [width // 2 + new_width // 2, height // 2 + new_height // 2, 1, 1])
    p1 = poly.insert_dot(p1, [width // 2 - new_width // 2, height // 2 + new_height // 2, 0, 1])

    # Lê a imagem da textura
    tex = cv2.imread("../assets/Press.png")

    # Cria uma cópia da imagem original
    animated_image = np.copy(image)
    pixel_step = int(min(width, height) * 0.3)
    # Loop para criar a animação
    while x2 < width and x3 >= 0:
        # Atualiza as coordenadas das retas
        
        x2 += pixel_step -50  # Aumenta x2 da esquerda para a direita
        x3 -= pixel_step  # Diminui x3 da direita para a esquerda
        
        # Atualiza as coordenadas dos círculos na coordenada y
        circle1_center_y += pixel_step *0.79 # Aumenta y do círculo azul para baixo
        circle2_center_y -= pixel_step *0.9  # Diminui y do círculo vermelho para cima, com velocidade maior
        
        # Cria a imagem animada com as retas e círculos atualizados
        animated_image = np.copy(image)
        
        # Adiciona as retas à imagem animada
        animated_image = img.strt_line(animated_image, x1, y1, x2, y2, intensity)
        animated_image = img.strt_line(animated_image, x3, y3, x4, y4, intensity2)

        
        # Cria os círculos
        circle1_points = poly.draw_circulo(circle1_center_x, circle1_center_y, circle1_radius)
        circle2_points = poly.draw_circulo(circle2_center_x, circle2_center_y, circle2_radius)
        
        # Adiciona os círculos à imagem animada
        animated_image = poly.set_circulo(animated_image, circle1_points, 0, 0, 255)  # Cor azul
        animated_image = poly.set_circulo(animated_image, circle2_points, 255, 0, 0)  # Cor vermelha
        
        # Adiciona os círculos menores no centro das pokebolas
        center_circle_radius = 3
        center_circle1_points = poly.draw_circulo(circle1_center_x, circle1_center_y, center_circle_radius)
        center_circle2_points = poly.draw_circulo(circle2_center_x, circle2_center_y, center_circle_radius)
        
        animated_image = poly.set_circulo(animated_image, center_circle1_points, 255, 255, 255)  # Cor branca
        animated_image = poly.set_circulo(animated_image, center_circle2_points, 255, 255, 255)  # Cor branca
        # Cria as elipses
        ellipse1_points = poly.draw_elipse(ellipse1_center_x, ellipse1_center_y, ellipse1_radius_x, ellipse1_radius_y)
        ellipse2_points = poly.draw_elipse(ellipse2_center_x, ellipse2_center_y, ellipse2_radius_x, ellipse2_radius_y)

        # Adiciona as elipses à imagem animada
        animated_image = poly.set_elipse(animated_image, ellipse1_points, 0, 255, 0)  # Cor verde
        animated_image = poly.set_elipse(animated_image, ellipse2_points, 255, 0, 255)  # Cor magenta   
        # Aplica o preenchimento com textura no polígono
        animated_image = img.scan_line(animated_image, p1, tex)
        
        # Exibe a imagem animada com o polígono texturizado
        cv2.imshow("Animation", animated_image)
        cv2.waitKey(1)  # Aguarda 1 milissegundo para atualizar a janela
        
        time.sleep(0.0001)

    cv2.waitKey(0)  # Aguarda uma tecla ser pressionada para encerrar
    cv2.destroyAllWindows()