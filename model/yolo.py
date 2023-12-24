from ultralytics import YOLO

def modelpicture(input_img):
    # モデル読み込み
    model = YOLO("yolov8n.pt")

    # 入力画像
    results = model(input_img,save=True)
    
if __name__ == "__main__":
    modelpicture('image/input/test1.jpg')