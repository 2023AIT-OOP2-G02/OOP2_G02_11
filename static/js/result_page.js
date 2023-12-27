const main_content = document.getElementById("main-content");
const title = document.title;

directory = "image/output/" + title;

// ファイル名を取得
let formData = new FormData();
formData.append("directory", directory);

fetch("/fetch_files_path", { method: "POST", body: formData }).then(response => {
    response.json().then((data) => {
        console.log(data.files_path);

        for (let filepath of data.files_path) {
            // 新しい画像オブジェクトを作成
            let img = new Image();

            // 画像のソースを設定
            img.src = filepath;  // 画像のパスを指定

            // 画像が読み込まれたら、それをbodyに追加
            img.onload = function () {
                main_content.appendChild(img);
            };
        }
    });
});
