function renderNoodleLogo() {
   var message = "Noodle";
   var colors = new Array("#4285F4","#EA4335","#FBBC05","#4285F4","#34A853","#EA4335"); // red, green, blue
   document.write("<strong>");
   for (var i = 0; i < message.length; i++)
      document.write("<span class=\"logo\" style=\"color:" + colors[(i % colors.length)] + ";\">" + message[i] + "</span>");
   document.write("</strong>");
}

