$(document).ready(function () {

    function handleButtonPress() {
        var track_id = $(this).data('track-id');
        $.get(`/verify?success=1&trackId=${track_id}&status=1`, function (response) {
            console.log('Response:', response);
        }).fail(function (xhr, status, error) {
            alert("Failed to verify transaction")
            console.log('Error:', status, error);
        }).always(function () {
            window.location.href = '/transactions';
        });
    }
    $('[verify-tx]').on('click', handleButtonPress);

});
