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
                width = img.width;
                height = img.height;

                // 画像のサイズを調整(縦横比を維持)
                scale = Math.min(280 / width, 196 / height);
                width = width * scale;
                height = height * scale;

                // 画像のサイズを設定
                img.width = width;
                img.height = height;

                div_rendering = document.createElement("div");
                div_rendering.width = 280;
                div_rendering.height = 196;
                div_rendering.className = "rendering";
                div_rendering.style.border = '1px solid black';
                div_rendering.style.margin = '2px';
                div_rendering.style.position = 'relative';
                div_rendering.appendChild(img);

                let a = document.createElement('a');
                a.textContent = filepath;
                a.href = filepath;      // リンク先を画像のURLに設定
                a.target = '_blank';    // 新しいタブでリンクを開く

                div_rendering.appendChild(a);
                main_content.appendChild(div_rendering);
            };
        }
    });
});
