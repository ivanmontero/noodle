$(document).ready(function() {
    $(".question").click(function() {
        // console.log($(this).attr("id"));      // Getting the ID of the clicked question
        // somehow get the question from python (and tell python to load it)
        $.ajax({
            url: "/questions/getquestion",
            data: {
                "question_id" :  $(this).attr("id")
            }
        }).then(function(result) {
            // Set overlay html with question. The result will be html
            $("#overlay").html( result );
        });
    });
});