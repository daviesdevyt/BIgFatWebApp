$(document).ready(function () {

    function handleButtonPress(event) {
        event.preventDefault();
        var pay_id = $(this).data('pay-id');
        $.get(`/verify/${pay_id}`, function (response) {
            $("#tx-status").html(response)
            console.log('Response:', response);
        }).fail(function (xhr, status, error) {
            alert("Failed to verify transaction")
            console.log('Error:', status, error);
        })
    }
    $('.verify-payment').on('click', handleButtonPress);

});
