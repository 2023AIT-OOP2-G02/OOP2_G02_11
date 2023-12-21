upload_button = document.getElementById("upload");
input_file = document.getElementById("file");
console.log(input_file);

let data = null;

input_file.addEventListener("change", function () {
    data = input_file.files[0];
    console.log(data);
});

upload_button.onclick = function () {
    let formData = new FormData();
    formData.append("data", data);
    
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
        console.log(response);
    })
}