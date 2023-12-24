import cv2

def outline_extract(filename): # 拡張子付き
    #グレースケールで読み込む
    path = 'image/input/' + filename
    input = cv2.imread(path, 0)

    #閾値
    threshold1 = 100
    threshold2 = 200
    #Cannyフィルタによる輪郭抽出
    output = cv2.Canny(input,threshold1,threshold2)
    #画像の出力
    # cv2.imshow("image",output)
    output_filename = filename.split('.')[0] + '_contour.jpg'
    cv2.imwrite("image/output/contour/" + output_filename, output)

    # cv2.waitKey()

if __name__ == "__main__":
    outline_extract('test2.jpg')