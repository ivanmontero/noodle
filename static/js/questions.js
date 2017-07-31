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