import cv2 as cv

def main():
    img = cv.imread('../images/lena.jpeg')
    imgGrayScale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    cv.namedWindow("Imagem em escala de cinza")
    cv.moveWindow("Imagem em escala de cinza", 375, 1)
    cv.imshow("Imagem em escala de cinza", imgGrayScale)

    cv.namedWindow("Imagem normal")
    cv.moveWindow("Imagem normal", 1, 1)
    cv.imshow("Imagem normal", img)
    
    cv.waitKey()
    cv.destroyAllWindows()

if __name__=="__main__":
    main()