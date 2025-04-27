import cv2 as cv

def main():
    img = cv.imread('../images/lena.jpeg')
    cv.imshow("Lena", img)
    cv.waitKey()
    cv.destroyAllWindows()   

if __name__ == "__main__":
    main()