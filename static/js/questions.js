$(document).ready(function() {
    $(".question").click(function() {
        // console.log($(this).attr("id"));      // Getting the ID of the clicked question
        // somehow get the question from python (and tell python to load it)
        $.ajax({
            url: "/questions/getquestionhtml",
            data: { "question_id" :  $(this).attr("id") }
        }).then(function(result) {
            // Set overlay html with question. The result will be html
            $("#overlay").html( result );
        });
        $("#overlay").css("display", "block");
    });
    $(".ask").click(function() {
        $.ajax("/questions/createquestion").then(function(result) {
            // Set overlay html with question. The result will be html
            $("#overlay").html( result );
        });
        $("#overlay").css("display", "block");
    });
    // $("#submit-question").click(function() {
    //     console.log("Question submit");
    //     $.post('/questions/newquestion', {
    //         "question" : $("#newquestiontitle").val(),
    //         "content" : $("#newquestionconent").val()
    //     });
    // });
    // TODO: transition
    $("#overlay").click(function() {
        if(!$(event.target).is('.post-item') && !$(event.target).parents('.post-item').is('.post-item') &&
             !$(event.target).is('#question-creation') && !$(event.target).parents('#question-creation').is('#question-creation')) {
            $("#overlay").css("display", "none");
        }
    });
});

function submitQuestion() {
    console.log("Question submit");
    console.log($("#newquestiontitle").val());
    console.log($("#newquestioncontent").val());
    $.post('/questions/newquestion', {
        "question" : $("#newquestiontitle").val(),
        "content" : $("#newquestioncontent").val()
    });
}