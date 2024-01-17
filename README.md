# OOP2_G02_11

## ライブラリのインストール
pip install -r requirements.txt


## 仕様

### 課題締切確認アプリ

#### 機能案

全ては時間の都合上実装できないので、アプリに必要な要素から順に実装していく。
大まかに上から実装していく予定。

- 教科ごとに出された課題をメモできる
- 課題の締め切りを定期的に通知
- 締め切りのどれくらい前に通知するかの設定
- 開いたらすぐに課題内容をメモできる
- 締切が近い順などの並び替え、絞り込み
- 先生が言った課題の重要ポイントをメモできる
- 提出方法なども見やすくメモできる
- 課題に必要な情報(参考にするサイトなど)をメモできる
- 提出し終わったらすぐにチェックできる
- 文字だけでなくスクショ、写真をメモに追加可能
- 落単カウンター
- 簡単にメモするためのテンプレート作成機能(ex.提出方法Moodle、期限一週間、教科ごとの独自の事項)
- 毎週ある課題は毎回設定しなくても通知される
- 提出先のサイトやアプリに飛べる
- 履修登録を参照できる
- カレンダー表示
- 携帯のホーム画面に表示
- 友達と課題の進捗を共有
- 課題の優先度を分ける
- 他のカレンダーアプリやiPhoneのカレンダーアプリの内容との連携
- moodleやlcamとの連携
- discordとbotと連携

#### 用いる技術

- Python
- flask
- HTML/CSS
- JavaScript
- SQLite
- localStorage
- プッシュ通知

### DBにPOST用の構造例(仮)

生成したUUIDをUserID、課題ID、画像IDとして割り当てて管理する予定
ユーザのUserIDの記憶はlocalStorageが担当

```json
{
    "fDja8VuaVy4BGNfXDL1ghm": { //課題id
        "title": "進捗報告作成",
        "deadline": "1/20",
        "subject": "オブ演",
        "memo": "感想いっぱい書く必要",
        "memo_img": "img/mCpcLbPq6pGf4ztYZsrKQi.jpg", //画像の保存名をUUIDにする
        "created_at": 1704963857047, //作成時刻(UNIX時間)
        "created_by": "aasa8Vuaty4BGNfXDL1ghm", //(user_id)
        "updated_at": 1704963857047 //更新時刻(UNIX時間)
    },
    "sFvind8np9Y9dD8wDVvxav": {
        "title": "だるい課題",
        "deadline": "1/30",
        "subject": "ぶつり",
        "memo": "たいへん",
        "memo_img": "img/uAhaHaJaYBA8FPchEJ9WCs.jpg",
        "created_at": 1704964105934,
        "created_by": "aasa8Vuaty4BGNfXDL1ghm",
        "updated_at": 1704964105934
    }
}
```

### ディレクトリ構成

#### main.py

flaskの制御を行うファイル

#### func.js

簡単なJS関数をまとめたファイル

#### templates

htmlのページを格納フォルダ

- index.html -> トップページ
- detail_edit_page.html -> 詳細＆編集ページ
- add_page.html -> 追加ページ
- remove_page.html -> 削除ページ
- search_page.html -> 検索ページ

#### static/css

cssを格納するフォルダ

#### sratic/js

jsを格納するフォルダ

#### model

main.pyでインスタンスを作って使用する、pythonクラスファイルを格納するフォルダ

#### img

画像名に画像IDを割り当てた画像を格納するフォルダ

## アプリ完成イメージ

![image](https://github.com/2023AIT-OOP2-G02/OOP2_G02_11/assets/109339477/1ec1a60f-0af1-4489-b643-7a9eed0e392b)
