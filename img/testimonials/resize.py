import cv2 as cv

im = cv.imread('proj5.png')

height, width = im.shape[:2]

thumbnail = cv.resize(im, (550, 400), interpolation = cv.INTER_AREA)

cv.imwrite('/home/pooja/Downloads/templatewire-interact/img/proj5.png',thumbnail)

cv.destroyAllWindows()
