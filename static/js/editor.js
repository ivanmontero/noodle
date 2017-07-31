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
});
// TODO: Format better

function renderNoodleLogo() {
   var message = "Noodle";
//    var colors = new Array("#4285F4","#EA4335","#FBBC05","#4285F4","#34A853","#EA4335"); // Google
//    var colors = new Array("#A7226E","#EC2049","#F26B38","#F7DB4F","#2F9599","#F7DB4F");
   var colors = new Array("#A7226E","#EC2049","#F26B38","#F7DB4F","#2F9599","#A7226E"); // Noodle
   document.write("<strong>");
   for (var i = 0; i < message.length; i++)
      document.write("<span class=\"logo-char hvr-grow\" style=\"color:" + colors[(i % colors.length)] + ";\">" + message[i] + "</span>");
   document.write("</strong>");
}