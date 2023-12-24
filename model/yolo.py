from ultralytics import YOLO
import cv2

# detection
def modelpicture(filename): # 拡張子付き
    
    # モデル読み込み
    model = YOLO("yolov8n.pt")

    # 入力画像のパスを指定して検出
    path = 'image/input/' + filename
    result = model(path)[0]
    
    result_img = result.plot()
    
    output_filename = filename.split('.')[0] + '_detection.jpg'
    cv2.imwrite('image/output/detection/' + output_filename, result_img)
    
if __name__ == "__main__":
    modelpicture('dog.jpg')