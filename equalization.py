import cv2
import matplotlib.pyplot as plt

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
