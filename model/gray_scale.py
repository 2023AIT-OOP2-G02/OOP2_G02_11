import cv2

im = cv2.imread('uchitane_near.png')

im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)

cv2.imwrite('image/output/grayscaleafter.png', im_gray_th_otsu)

