import threading

from flask import Flask, request, render_template, jsonify, Blueprint
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

from model.watch_dir import start_watchdog
from get_imgs_filepath import get_images_filepath
from get_imgs_filepath import get_filenames


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# 静的ディレクトリの追加
add_app = Blueprint("image", __name__,
                    static_url_path="/image", static_folder="./image")
app.register_blueprint(add_app)

# ディレクトリの監視を並列で開始
directory_to_watch = "./image/input"  # 保存先
thread = threading.Thread(target=start_watchdog, args=(directory_to_watch,))
thread.daemon = True    # メインスレッドが終了したら、スレッドも終了する
thread.start()


# http://127.0.0.1:5000/
@app.route('/')
def index():
    # このコードは上に書いたほうが良い気がする (変更済み)
    # # ディレクトリの監視を並列で開始
    # directory_to_watch = "./image/input"  # 保存先
    # thread = threading.Thread(target=start_watchdog, args=(directory_to_watch,))
    # thread.start()

    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    try:
        # 画像dataの取得
        data = request.files.get('data')  # TODO

        # image/inputに保存
        data.save('image/input/' + data.filename)

        # TODO: 画像の処理
    except Exception as e:
        print(e)
        return jsonify({
            "error": "画像の保存に失敗しました。"
        })

    return jsonify({
        "success": "画像の保存に成功しました。"
    })


@app.route('/fetch_files_path', methods = ['POST'])
def fetch_files_path():
    directory = request.form['directory']
    files_path = get_images_filepath(directory)
    
    return jsonify({
        "files_path": files_path
    })


# モザイク
@app.route('/mosaic')
def mosaic():
    return render_template("mosaic.html")


# 枠で囲む
@app.route('/frame')
def frame():
    return render_template("frame.html")


# 輪郭抽出
@app.route('/contour')
def contour():
    return render_template("contour.html")


# グレイスケール
@app.route('/grayscale')
def grayscale():
    return render_template("grayscale.html")


# 物体検出
@app.route('/detection')
def detection():
    return render_template("detection.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)
