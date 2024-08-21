import cv2
import matplotlib.pyplot as plt
from utils import salvar_histogramas

def calcular_mostrar_histogramas(image1, image2):
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    gray_image1 = cv2.cvtColor(image1_rgb, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2_rgb, cv2.COLOR_BGR2GRAY)
    hist_image1 = cv2.calcHist([image1_rgb], [0], None, [256], [0, 256])
    hist_image2 = cv2.calcHist([image2_rgb], [0], None, [256], [0, 256])
    hist_gray_image1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    hist_gray_image2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])
    hist_bgr_image1 = [cv2.calcHist([image1], [i], None, [256], [0, 256]) for i in range(3)]
    hist_bgr_image2 = [cv2.calcHist([image2], [i], None, [256], [0, 256]) for i in range(3)]

    print("Escolha o que deseja fazer:")
    print("a - Calcular e mostrar os respectivos histogramas das imagens originais")
    print("b - Imagem 1 e 2 em tons de cinza e seus histogramas")
    print("c - Imagens em colorido (BGR plot)")
    sub_choice = input("Escolha uma opção: ")

    if sub_choice == 'a':
        titles = ['Imagem 1', 'Histograma Imagem 1', 'Imagem 2', 'Histograma Imagem 2']
        images = [image1_rgb, hist_image1, image2_rgb, hist_image2]
        plt.figure(figsize=(10, 8))
        for i in range(4):
            plt.subplot(2, 2, i + 1)
            if i % 2 == 1:
                plt.plot(images[i])
                plt.title(titles[i])
                plt.xlim([0, 256])
            else:
                plt.imshow(images[i])
                plt.title(titles[i])
                plt.axis('off')
        salvar_histogramas([hist_image1, hist_image2], 'original')

    elif sub_choice == 'b':
        titles = ['Imagem 1 - Tons de Cinza', 'Histograma Imagem 1 - Tons de Cinza', 'Imagem 2 - Tons de Cinza', 'Histograma Imagem 2 - Tons de Cinza']
        images = [gray_image1, hist_gray_image1, gray_image2, hist_gray_image2]
        plt.figure(figsize=(10, 8))
        for i in range(4):
            plt.subplot(2, 2, i + 1)
            if i % 2 == 1:
                plt.plot(images[i])
                plt.title(titles[i])
                plt.xlim([0, 256])
            else:
                plt.imshow(images[i], cmap='gray')
                plt.title(titles[i])
                plt.axis('off')
        salvar_histogramas([hist_gray_image1, hist_gray_image2], 'gray')

    elif sub_choice == 'c':
        titles = ['Imagem 1 - BGR', 'Histograma Imagem 1 - BGR', 'Imagem 2 - BGR', 'Histograma Imagem 2 - BGR']
        images = [image1, hist_bgr_image1, image2, hist_bgr_image2]
        colors = ['b', 'g', 'r']
        plt.figure(figsize=(10, 8))
        for i in range(4):
            plt.subplot(2, 2, i + 1)
            if i % 2 == 1:
                for j, color in enumerate(colors):
                    plt.plot(images[i][j], color=color)
                plt.title(titles[i])
                plt.xlim([0, 256])
            else:
                plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
                plt.title(titles[i])
                plt.axis('off')
        salvar_histogramas(hist_bgr_image1 + hist_bgr_image2, 'bgr')

    else:
        print("Opção inválida. Por favor, escolha a, b ou c.")
    
    plt.tight_layout()
    plt.show()

def calcular_mostrar_histogramas_gray(image1, image2):
    hist_image1 = cv2.calcHist([image1], [0], None, [256], [0, 256])
    hist_image2 = cv2.calcHist([image2], [0], None, [256], [0, 256])
    titles = ['Imagem 1 - Tons de Cinza', 'Histograma Imagem 1', 'Imagem 2 - Tons de Cinza', 'Histograma Imagem 2']
    images = [image1, hist_image1, image2, hist_image2]
    plt.figure(figsize=(10, 8))
    for i in range(4):
        plt.subplot(2, 2, i + 1)
        if i % 2 == 1:
            plt.plot(images[i])
            plt.title(titles[i])
            plt.xlim([0, 256])
        else:
            plt.imshow(images[i], cmap='gray')
            plt.title(titles[i])
            plt.axis('off')
    salvar_histogramas([hist_image1, hist_image2], 'gray_images')
    plt.tight_layout()
    plt.show()
