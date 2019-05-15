$(document).ready(function () {

    $("#generateQrCode").click(function (event) {
        event.stopPropagation();
        $("#qrCodeBox").show();
        $.post("/generateQRCode", function (data) {
            $("#qrCode").attr("src", "/static/image/qrcode.jpg");
        })
    });

    $(document).click(function () {
        $("#qrCodeBox").hide();
    })
});