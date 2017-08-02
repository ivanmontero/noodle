// $(document).ready( function() {
//     $("#submit").click(function(){
    function shareCode() {
        $.post({
            url: "/share",
            success: function(response) {
                $("p").text("Share your code using this link: be-noodley.appspot.com/share?key=" + response);
            }
        });
    }
//     });
// });