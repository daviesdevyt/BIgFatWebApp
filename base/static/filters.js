var custom_filter_values = {}

$(`.bf-filter-dropdown input`).click(function(){
    let value = $(this).data("value-id")
    let prop = $(this).prop("name")
    if (this.checked) {
        custom_filter_values[prop] = value
    }
    else {
        delete custom_filter_values[prop]
    }
    console.log(value, prop)
    console.log(custom_filter_values)
    if (Object.keys(custom_filter_values).length === 0){
        $("[data-loading-text]").html("No selected filters")
        $("#ocfilter-button button").addClass("disabled")
        return;
    }
    $("[data-loading-text]").html("Show products")
    $("#ocfilter-button button").removeClass("disabled")
})

$("#ocfilter-button button").on("click", function(){
    let url = new URL(window.location.href)
    for (let prop in custom_filter_values) {
        console.log(prop)
        url.searchParams.set(prop, custom_filter_values[prop])
    }
    console.log(url.href)
    window.location.href = url.href
})
