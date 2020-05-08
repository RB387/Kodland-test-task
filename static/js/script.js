function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#id_image').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

function bind_image_uploader() {
    $("#image-upload").change(function () {
        readURL(this);
    });
}