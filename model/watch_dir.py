import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from model.face_detect_rectangle import detect_face
from model.face_mosaic import face_mosaic
from model.gray_scale import gray_scale
from model.outline_extraction import outline_extract
from model.yolo import modelpicture


# ディレクトリを監視
class DirWatcher(FileSystemEventHandler):
    def on_created(self, event):
        # ディレクトリは弾く
        if event.is_directory:
            print(f"ディレクトリが作成されました。: {event.src_path}")
            return

        # ファイル名のみを取得
        file_name = event.src_path.split("\\")[-1]
        print(f"ファイルが作成されました。: {file_name}")

        # 画像処理
        # 処理後はimage/outputに保存
        try:
            detect_face(file_name)
            face_mosaic(file_name)
            gray_scale(file_name)
            outline_extract(file_name)
            modelpicture(file_name)

        except Exception as e:
            print(e)
            print("画像処理に失敗しました。")
            return

        print("画像処理が完了しました。")

# ディレクトリ監視を開始する関数
def start_watchdog(directory_path):
    dir_watcher = DirWatcher()
    observer = Observer()
    observer.schedule(dir_watcher, path=directory_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


# テスト用
# if __name__ == "__main__":
#     directory_to_watch = "../image/input"
#     start_watchdog(directory_to_watch)
