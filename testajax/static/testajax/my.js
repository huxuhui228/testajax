$("#amenu").click(function () {
    console.log("amenu clicked.");
    $.ajax({
        url:"/ajax",
        type:"GET",    
        success: function (data) {
            console.log(data);
            $("#main").html(data);
        }
    })
})