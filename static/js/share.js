 $(document).ready( function() {
    $("#submit").click(function(){
        $.post({
            url: "/share",
            data: {
                code: $("#code").val()
            },
            success: function(unique_id) {
                console.log(unique_id);
                $("#share-link").text("Share your code using this link: be-noodley.appspot.com/share?key=" + unique_id);
            }
        });
    });

    $("#start").click(function(){
        $("#share-main-menu").css("display", "none");
        $("#code-share-hide").css("display", "block");
    })
});