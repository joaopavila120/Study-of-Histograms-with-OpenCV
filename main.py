import cv2
from histogram import calcular_mostrar_histogramas, calcular_mostrar_histogramas_gray
from equalization import equalizar_imagens

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
