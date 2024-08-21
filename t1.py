import cv2
import numpy as np
import matplotlib.pyplot as plt

def salvar_histogramas(histogramas, nome_base):
    for i, hist in enumerate(histogramas):
        intensidade = np.arange(256)
        hist_data = np.hstack((intensidade.reshape(-1, 1), hist))
        np.savetxt(f'{nome_base}_hist{i}.csv', hist_data, delimiter=',', header='Intensidade,Contagem', comments='', fmt='%d')

def calcular_mostrar_histogramas(image1, image2):
    image1_rgb       = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    image2_rgb       = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    gray_image1      = cv2.cvtColor(image1_rgb, cv2.COLOR_BGR2GRAY)
    gray_image2      = cv2.cvtColor(image2_rgb, cv2.COLOR_BGR2GRAY)
    hist_image1      = cv2.calcHist([image1_rgb], [0], None, [256], [0, 256])
    hist_image2      = cv2.calcHist([image2_rgb], [0], None, [256], [0, 256])
    hist_gray_image1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    hist_gray_image2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])
    hist_bgr_image1  = [cv2.calcHist([image1], [i], None, [256], [0, 256]) for i in range(3)]
    hist_bgr_image2  = [cv2.calcHist([image2], [i], None, [256], [0, 256]) for i in range(3)]

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

def equalizar_imagens(image1, image2):
    equalized_image1 = cv2.equalizeHist(image1)
    equalized_image2 = cv2.equalizeHist(image2)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_image1 = clahe.apply(image1)
    clahe_image2 = clahe.apply(image2)
    titles = ['Imagem 1 - Equalização CDF', 'Imagem 1 - Equalização CLAHE', 'Imagem 2 - Equalização CDF', 'Imagem 2 - Equalização CLAHE']
    images = [equalized_image1, clahe_image1, equalized_image2, clahe_image2]
    plt.figure(figsize=(12, 8))
    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()

print("Selecione o que quer fazer:")
print("1 - Carregar duas imagens, calcular e mostrar os respectivos histogramas")
print("2 - Carregar outras duas imagens com diferentes tons de cinza")
choice = input("Escolha uma opção: ")

if choice == '1':
    image1 = cv2.imread('images/image1.jpg')
    image2 = cv2.imread('images/image2.jpg')

    if image1 is None or image2 is None:
        print("Erro: Não foi possível carregar uma ou ambas as imagens.")
    else:
        calcular_mostrar_histogramas(image1, image2)

elif choice == '2':
    image1_gray = cv2.imread('images_gray/gray_image1.jpg', cv2.IMREAD_GRAYSCALE)
    image2_gray = cv2.imread('images_gray/gray_image2.jpg', cv2.IMREAD_GRAYSCALE)

    if image1_gray is None or image2_gray is None:
        print("Erro: Não foi possível carregar uma ou ambas as imagens em tons de cinza.")
    else:
        print("Escolha o que deseja fazer:")
        print("a - Calcular e apresentar seus histogramas")
        print("b - Rodar uma equalização com o método CDF e outra com o método CLAHE")
        sub_choice = input("Escolha uma opção: ")

        if sub_choice == 'a':
            calcular_mostrar_histogramas_gray(image1_gray, image2_gray)
        elif sub_choice == 'b':
            equalizar_imagens(image1_gray, image2_gray)
        else:
            print("Opção inválida. Por favor, escolha a ou b.")

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
