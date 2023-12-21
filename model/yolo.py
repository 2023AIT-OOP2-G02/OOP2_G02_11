from ultralytics import YOLO

def modelpicture(img):
    # モデル読み込み
    model = YOLO("yolov8n.pt")

    # 入力画像
    model(img, save=True)
modelpicture('test3.jpeg')