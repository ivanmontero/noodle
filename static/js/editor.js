$(document).ready(function() {
    // To update the iframe
    $("#input").on('input', function() {
        $("iframe").attr("srcdoc", $("#input").val());
        console.log("change");
    });
    // To allow tabs
    $(document).delegate('#input', 'keydown', function(e) {
        var keyCode = e.keyCode || e.which;

        if (keyCode == 9) {
            e.preventDefault();
            var start = $(this).get(0).selectionStart;
            var end = $(this).get(0).selectionEnd;

            // set textarea value to: text before caret + tab + text after caret
            $(this).val($(this).val().substring(0, start)
                        + "\t"
                        + $(this).val().substring(end));

            // put caret at right position again
            $(this).get(0).selectionStart =
            $(this).get(0).selectionEnd = start + 1;
        }
    });

    $("#start").click(function(){
        $("#main-editor").css("display", "none");
        $("#editor").css("display", "block");
    })
});

// TODO: Format better