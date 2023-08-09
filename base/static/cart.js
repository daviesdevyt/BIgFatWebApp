$(document).ready(function () {

    function handleButtonPress() {
        var productId = $(this).data('product-id');
        $.get('/add-cart/'+productId, function (response) {
            flash_message("Added to cart!", "success")
        }).fail(function (xhr, status, error) {
            alert("Failed to add to cart")
            console.log('Error:', status, error);
        }).done(function (response) {
            $(".cart-count").html(response)
        });
    }
    $('.addcart').on('click', handleButtonPress);
    
});
function flash_message(message, theme){
    template = `<div class="bf-article-inner flash-message ${theme}">${message}</div>`
    $("#messages").html(template)
}