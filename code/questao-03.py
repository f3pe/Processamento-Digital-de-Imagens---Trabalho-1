import cv2 as cv
from matplotlib import pyplot as plt

def main():
    # Carregando cada canal
    blue = cv.imread("images/Demon_Azul.jpg", 0)
    green = cv.imread("images/Demon_Verde.jpg", 0)
    red = cv.imread("images/Demon_Vermelho.jpg", 0)

    # Juntando as imagens
    img = cv.merge([blue, green, red])

    #Convertendo de BGR para RGB
    blue = cv.cvtColor(blue, cv.COLOR_BGR2RGB)
    green = cv.cvtColor(green, cv.COLOR_BGR2RGB)
    red = cv.cvtColor(red, cv.COLOR_BGR2RGB)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    plt.subplot(2, 3, 1)
    plt.imshow(red)
    plt.title("Canal Vermelho")
    plt.axis("off")

    plt.subplot(2, 3, 2)
    plt.imshow(green)
    plt.title("Canal Verde")
    plt.axis("off")

    plt.subplot(2, 3, 3)
    plt.imshow(blue)
    plt.title("Canal Azul")
    plt.axis("off")

    plt.subplot(2, 3, 5)
    plt.imshow(img)
    plt.title("Imagem Colorida")
    plt.axis("off")

    plt.show()


if __name__=="__main__":
    main()