function handleButtonPress() {
    var productId = $(this).data('product-id');
    $(this).addClass("adding")
    $(this).prop("disabled", true)
    var btn = $(this)
    $.get('/add-cart/' + productId, function (response) {
        btn.removeClass("adding")
        btn.addClass('check');
        $(".cart-count").html(response)
    }).fail(function (xhr, status, error) {
        flash_message("Failed to add to cart", "error")
        $(this).addClass("disabled", false)
    })
}
$('.addcart').on('click', handleButtonPress);

function flash_message(message, theme) {
    template = `<div class="bf-article-inner flash-message ${theme}">${message}</div>`
    $("#messages").html(template)
}

function creditChecker() {
    var productId = $(this).data('product-id');
    $(this).prop("disabled", true)
    $(this).addClass("waiting")
    $(this).html(`<img src="https://bigfat.cc/catalog/view/theme/bigfat/images/ajax.svg" />`)
    var btn = $(this)
    $.get("/cc-checker/" + productId, function (response) {
        if (response.code != 200) {
            flash_message(response.message, "error")
            $(this).prop("disabled", false)
        }
        else {
            $(this).addClass(response.status)
        }
    }).always(function () {
        btn.html("")
        btn.removeClass("waiting")
    })

}

$(".bf-table-checker").on("click", creditChecker)