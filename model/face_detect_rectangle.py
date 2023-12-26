import cv2


def detect_face(filename):  # 拡張子付き

    # 顔検出器の読み込み
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # 画像の読み込み
    path = 'image/input/' + filename
    img = cv2.imread(path)

    # 画像をグレースケールに変換
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    facerect = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

    # 顔の数だけ処理
    if len(facerect) > 0:
        for rect in facerect:
            # 矩形描画
            cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), (255, 255, 255), 3)

    output_filename = filename.split('.')[0] + '_face.jpg'
    cv2.imwrite('image/output/frame/' + output_filename, img)


if __name__ == "__main__":
    # 認識制度が低い
    detect_face('human.jpg')
