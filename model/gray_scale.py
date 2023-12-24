import cv2

def gray_scale(filename): # 拡張子付き
    
    path = 'image/input/' + filename
    im = cv2.imread(path)

    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)

    output_filename = filename.split('.')[0] + '_gray.jpg'
    cv2.imwrite('image/output/grayscale/' + output_filename, im_gray_th_otsu)

if __name__ == "__main__":
    gray_scale('cat.jpg')