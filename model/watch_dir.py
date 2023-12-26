import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# ディレクトリを監視
class DirWatcher(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            # ファイル名のみを取得
            file_name = event.src_path.split("/")[-1]
            print(f"ファイルが作成されました。: {file_name}")

            # 画像処理






        else:
            print(f"ディレクトリが作成されました。: {event.src_path}")


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
