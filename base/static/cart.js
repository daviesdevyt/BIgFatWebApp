$(document).ready(function () {

    function handleButtonPress() {
        var productId = $(this).data('product-id');
        $.get('/add-cart/'+productId, function (response) {
            console.log('Response:', response);
        }).fail(function (xhr, status, error) {
            alert("Failed to add to cart")
            console.log('Error:', status, error);
        });
    }

    $('.addcart').on('click', handleButtonPress);

});
function removeFromCart(prod_id){
    $.get('/delete-cart/'+prod_id, function (response) {
        console.log('Response:', response);
    }).fail(function (xhr, status, error) {
        alert("Failed to remove from cart")
        console.log('Error:', status, error);
    });
}