//Variables
const verification = document.getElementById("verification-code");

//functions
function setInputFilter(textbox, inputFilter) {
    ["input", "keydown", "keyup", "mousedown", "mouseup", "select", "contextmenu", "drop"].forEach(function(event) {
      textbox.addEventListener(event, function() {
        if (inputFilter(this.value)) {
          this.oldValue = this.value;
          this.oldSelectionStart = this.selectionStart;
          this.oldSelectionEnd = this.selectionEnd;
        } else if (this.hasOwnProperty("oldValue")) {
          this.value = this.oldValue;
          this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
        } else {
          this.value = "";
        }
      });
    });
  }

//events
// if (verification.value)
function check(){
    const verifyLength = verification.value
    console.log(verifyLength.length)
    if(verifyLength.length == 6){
        document.getElementById("verification").submit();
    }
}

  
// Install input filters.
setInputFilter(verification, function(value) {
    return /^-?\d*$/.test(value); 
});

function reco(){
  if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
  }
}

