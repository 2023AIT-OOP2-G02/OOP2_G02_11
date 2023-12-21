import cv2

#グレースケールで読み込む
input_name = 'uchitane_near.png'
input = cv2.imread(input_name, 0)

#閾値
threshold1 = 100
threshold2 = 200
#Cannyフィルタによる輪郭抽出
output = cv2.Canny(input,threshold1,threshold2)
#画像の出力
cv2.imshow("image",output)
#cv2.imwrite("output", output)

cv2.waitKey()

