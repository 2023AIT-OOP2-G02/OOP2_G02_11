import os
import glob


# input と　output のimgを削除する
def delete_image_files(directory):
    # 対応する画像ファイルの拡張子
    extensions = ['*.png', '*.jpg', '*.jpeg']

    for ext in extensions:
        # os.path.joinを使用してディレクトリと拡張子を結合
        image_files = glob.glob(os.path.join(directory, ext))

        # 各画像ファイルを削除
        for image_file in image_files:
            os.remove(image_file)
            print(f"Deleted: {image_file}")


if __name__ == "__main__":
    delete_image_files('image/input')
    delete_image_files('image/output/contour/')
    delete_image_files('image/output/detection/')
    delete_image_files('image/output/frame/')
    delete_image_files('image/output/grayscale/')
    delete_image_files('image/output/mosaic/')
