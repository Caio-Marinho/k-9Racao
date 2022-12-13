var formID = document.getElementById("incremento");
var send = $("#plus") && $("#minus");

$(formID).submit(function(event){
  if (formID.checkValidity()) {
    send.attr('disabled', 'disabled');
  }
});