// DOMの取得
const upload_button = document.getElementById("upload");
const input_file = document.getElementById("file");
const errorContainer = document.getElementById("error-container");
const successContainer = document.getElementById("success-container");

// console.log(input_file);

let data = null;

input_file.addEventListener("change", function () {
    data = input_file.files[0];
    // console.log(data);
});

// アップロードボタンが押下時の処理
upload_button.onclick = function () {
    // メッセージコンテナを非表示に
    errorContainer.style.display = "none";
    successContainer.style.display = "none";

    // データ送信用のフォーマットを作成
    let formData = new FormData();
    formData.append("data", data);

    // flaskにデータを送信
    // 送信先 : /upload
    fetch("/upload", {method: "POST", body: formData}).then(response => {
        response.json().then((data) => {
            console.log(data);
            //失敗
            if (data.error) {
                errorContainer.innerText = data.error;
                errorContainer.style.display = "inline-block";
            //成功
            } else if (data.success) {
                successContainer.innerText = data.success;
                successContainer.style.display = "inline-block";
            //不明なエラー
            } else {
                errorContainer.innerText = "不明なエラーが発生しました。";
                errorContainer.style.display = "inline-block";
            }

        });
    });
}

// $.ajax({
//     url: "/upload",
//     type: "POST",
//     data: formData,
//     cache: false,
//     contentType: false,
//     processData: false,
//     dataType: 'text',
// })
// .done(function (response) { //responseはjson形式
//     // if (response.success === ) {
//     //     alert("アップロードに成功しました");
//     // }
//     // '/upload'の返り値を出力
//
//     response.json().then((data) => {
//         console.log(data);
//     });
//
// })