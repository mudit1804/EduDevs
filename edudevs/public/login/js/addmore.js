
var key=0;
var val=0;

function add_fields() {

key++;
val++;

document.getElementById('total').value = key;

var objTo = document.getElementById('mfields');
var divtest = document.createElement("div");

// divtest.innerHTML = '<div class="col-mod-6"><label>Email Id: #' + key + '</label> <input type="text" name="email' + key + '"/> </div>';   
divtest.innerHTML = '<div class="col-mod-6"><label>Email Id: #' + key + '</label> <input type="text" name="email' + key + '"/> </div>';   

objTo.appendChild(divtest)
}



