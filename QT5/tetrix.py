import numpy
import cv2

class LoadImage:
    def loadImage(self):
        img = cv2.imread('photo.jpg')
        cv2.imshow('Image on a window',img)
        k = cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()
        elif k == ord('s'):
            cv2.imwrite('photopng.png',img)
            cv2.destroyAllWindows()

if __name__=="__main__":
    LI=LoadImage()
    LI.loadImage()
