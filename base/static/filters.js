var custom_filter_values = {}

$(".bf-sort-button-select").on("click", function(e){
    prop = $(this).data("prop")
    is_checked = $(this).hasClass("check")
    if (is_checked){
        delete custom_filter_values[prop]
    }
    else{
        custom_filter_values[prop] = true
    }
    filters_btn_function()
})

$(".search_title").on("change", function(){
    custom_filter_values["cc"] = $(this).val()
    filters_btn_function()
})

function filters_btn_function () {
    if (Object.keys(custom_filter_values).length === 0){
        $("[data-loading-text]").html("No selected filters")
        $("#ocfilter-button button").addClass("disabled")
        return;
    }
    $("[data-loading-text]").html("Show products")
    $("#ocfilter-button button").removeClass("disabled")
}

$(`.bf-filter-dropdown input`).click(function(){
    let value = $(this).data("value-id")
    let prop = $(this).prop("name")
    if (this.checked) {
        custom_filter_values[prop] = value
    }
    else {
        delete custom_filter_values[prop]
    }
    filters_btn_function()
})

$("#ocfilter-button button").on("click", function(){
    let url = new URL(window.location.href)
    url.search = "";
    for (let prop in custom_filter_values) {
        url.searchParams.set(prop, custom_filter_values[prop])
    }
    window.location.href = url.href
})
