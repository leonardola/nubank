$(document).ready(function () {

    $("#generateQrCode").click(function (event) {
        event.stopPropagation();
        $("#qrCodeBox").show();
        $.post("/generateQRCode", function (data) {
            $("#qrCode").attr("src", "/static/image/qrcode.jpg");
            $("#qrCode").attr("uuid", data.uuid);
        })
    });

    $("#qrCodeBox").click(function () {
        var uuid = $("#qrCode").attr("uuid");
        $.post("/generateQRCode/"+uuid, function () {
            $("#qrCodeBox").hide();
            location.reload(true);
        }).fail(function () {
            alert("Falha ao sincronizar");
        });
    });

    $(document).click(function () {
        $("#qrCodeBox").hide();
    })
});