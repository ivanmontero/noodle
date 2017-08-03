$(document).ready(function() {
    $(document).on("click", ".question", function() {
        // console.log($(this).attr("id"));      // Getting the ID of the clicked question
        // somehow get the question from python (and tell python to load it)
        $.ajax({
            url: "/questions/getquestionhtml",
            data: { "question_id" :  $(this).attr("id") }
        }).then(function(result) {
            // Set overlay html with question. The result will be html
            // OLD
            $("#overlay").html( result );
            // NEW
            // $("#overlay").html("")
            //              .append(htmlToElements(result));
            
        });
        $("#overlay").height($(document).height());
        $("#overlay").css("display", "block");
    });
    $(document).on("click", ".ask", function() {
        $.ajax("/questions/createquestion").then(function(result) {
            // Set overlay html with question. The result will be html
            $("#overlay").html( result );
            // $("#overlay").html("")
            //              .append(htmlToElements(result));
        });
        $("#overlay").height($(document).height());
        $("#overlay").css("display", "block");
    });
    $(document).on('click', '#submit-question', function(){
        console.log("Question submit");
        // console.log($("#newquestiontitle").val());
        // console.log($("#newquestioncontent").val());
        $.post('/questions/newquestion', {
            "question" : $("#newquestiontitle").val(),
            "content" : $("#newquestioncontent").val()
        });
        $("#overlay").css("display", "none");
        // PROBLEMATIC
        setTimeout(function() {
            // SHOW DESCRIPTION NO LONGER WORKS ON ELEMENTS AFTER SUBMIT
            // FIXED
            $.ajax("/questions/getquestionshtml").then(function(result) {
                console.log(result);
                $(".recent").html(result);
            });
        } , 1000);
        
    // what you want to happen when mouseover and mouseout 
    // occurs on elements that match '.dosomething'
    });
    $(document).on('click', '#submit-answer', function(){
            console.log("Answer submit");
            // console.log($("#newquestiontitle").val());
            // console.log($("#newquestioncontent").val());
            console.log($("#current-question-id").text());
            console.log($("#new-answer").val());
            $.post('/questions/newanswer', {
                "question_id" : $("#current-question-id").text(),
                "content" : $("#new-answer").val()
            });
            // $("#overlay").css("display", "none");
            // PROBLEMATIC
            setTimeout(function() {
                // SHOW DESCRIPTION NO LONGER WORKS ON ELEMENTS AFTER SUBMIT
                // FIXED
                $.ajax({
                    url: "/questions/getquestionhtml",
                    data: { "question_id" :  $("#current-question-id").text() }
                }).then(function(result) {
                    // Set overlay html with question. The result will be html
                    // OLD
                    $("#overlay").html( result );
                    // NEW
                    // $("#overlay").html("")
                    //              .append(htmlToElements(result));
                    
                });
                $("#overlay").height($(document).height());
            } , 1000);
            
        // what you want to happen when mouseover and mouseout 
        // occurs on elements that match '.dosomething'
    });
    // $.ajax("/questions/getquestionshtml").then(function(result) {
    //     console.log(result);
    //     $(".recent").html(result);
    // });
    // $("#submit-question").click(function() {
    //     console.log("Question submit");
    //     $.post('/questions/newquestion', {
    //         "question" : $("#newquestiontitle").val(),
    //         "content" : $("#newquestionconent").val()
    //     });
    // });
    // TODO: transition
    $(document).on("click", "#overlay", function() {
        // if(!$(event.target).is('.post-item') && !$(event.target).parents('.post-item').is('.post-item') &&
        //      !$(event.target).is('#question-creation') && !$(event.target).parents('#question-creation').is('#question-creation')) {
        if(!$(event.target).is('.not-redirectable') && !$(event.target).parents('.not-redirectable').is('.not-redirectable'))
            $("#overlay").css("display", "none");
    });

    // $(window).resize(function() {
    //     $('#overlay').height(function(index, height) {
    //         return window.innerHeight - $(this).offset().top;
    //     });
    // });
});

// function submitQuestion() {
//     // console.log("Question submit");
//     // console.log($("#newquestiontitle").val());
//     // console.log($("#newquestioncontent").val());
//     $.post('/questions/newquestion', {
//         "question" : $("#newquestiontitle").val(),
//         "content" : $("#newquestioncontent").val()
//     });
//     $("#overlay").css("display", "none");
// }

// function htmlToElements(html) {
//     var template = document.createElement('template');
//     template.innerHTML = html;
//     return template.content.childNodes;
// }