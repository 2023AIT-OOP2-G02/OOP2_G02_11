import os
import glob


def get_images_filepath(directory):
    # 対応する画像ファイルの拡張子
    extensions = ['*.png', '*.jpg',]

    image_files = []
    for ext in extensions:
        # os.path.joinを使用してディレクトリと拡張子を結合
        image_files.extend(glob.glob(os.path.join(directory, ext)))

    # path
    return image_files


if __name__ == "__main__":
    # 使用例
    directory = 'image/output/mosaic/'  # 画像ファイルを探すディレクトリ
    image_files = get_images_filepath(directory)

    # 結果を表示
    for image_file in image_files:
        print(image_file)
