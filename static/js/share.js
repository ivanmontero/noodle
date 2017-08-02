 $(document).ready( function() {
    $("#submit").click(function(){
        console.log("jdaslfhusdahlfjkhdsakfhasdkjhflkahsdlkjfhjaksd");
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
});