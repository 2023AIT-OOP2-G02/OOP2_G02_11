import cv2


# path = "tokage28_11.jpg" # テスト用の画像

# 画像から顔を検出、モザイクをかける
def face_mosaic(filename):  # 拡張子付き
    # 画像の読み込み
    path = 'image/input/' + filename
    img = cv2.imread(path)

    # 顔検出器の読み込み
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # 画像をグレースケールに変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔の検出
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 各顔にモザイクをかける
    for (x, y, w, h) in faces:
        # 顔の領域を切り抜く
        face = img[y:y + h, x:x + w]

        # モザイク処理
        face = cv2.resize(face, (50, 50), interpolation=cv2.INTER_LINEAR)
        face = cv2.resize(face, (w, h), interpolation=cv2.INTER_NEAREST)

        # モザイクをかけた顔を元の画像に貼り付ける
        img[y:y + h, x:x + w] = face

    # モザイクをかけた画像を保存
    output_filename = filename.split('.')[0] + '_mosaic.jpg'
    cv2.imwrite("image/output/mosaic/" + output_filename, img)


if __name__ == "__main__":
    face_mosaic('human.jpg')
