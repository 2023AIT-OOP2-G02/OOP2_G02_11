
// アップロードボタン
upload_button = document.getElementById("upload");
// ファイル選択ボタン
input_file = document.getElementById("file");
console.log(input_file);

let data = null;

input_file.addEventListener("change", function () {
    data = input_file.files[0];
    console.log(data);
});

// アップロードボタンが押下時の処理
upload_button.onclick = function () {
    // データ送信用のフォーマットを作成
    let formData = new FormData();
    formData.append("data", data);

    // flaskにデータを送信
    $.ajax({
        url: "/upload",
        type: "POST",
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        dataType: 'text',
    })
    .done(function (response) {
        // '/upload'の返り値を出力
        console.log(response);
    })
}