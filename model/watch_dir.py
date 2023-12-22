import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# ディレクトリを監視
class DirWatcher(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"ファイルが作成されました: {event.src_path}")
        else:
            print(f"File created: {event.src_path}")


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


if __name__ == "__main__":
    directory_to_watch = "../image/input"
    start_watchdog(directory_to_watch)
