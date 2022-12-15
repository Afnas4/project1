var nam=document.getElementById("name");
var email=document.getElementById("email");
var pass1=document.getElementById("pass1");
var pass2=document.getElementById("pass2");
var ph=document.getElementById("num");

function validname(){
    var fn=nam.value;
    if (isNaN(fn)){
        nam.className= "success";
        document.getElementById("text").innerHTML= "";
    } 
    else{
        nam.className="error";
        document.getElementById("signup").disabled=true;
        document.getElementById("text").innerHTML = "please enter name";
    }
}
function validemail(){
    var mail=email.value;
    var re=/^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$/;
    if(re.test(mail)){
        email.className="success";
        document.getElementById("text").innerHTML="";
    }else{
        email.className="error";
        document.getElementById("signup").disabled=true;
        document.getElementById("text").innerHTML = "please enter valid email";
}
}
function validph(){
    var num=ph.value;
    if (isNaN(num)){
        ph.className="error";
        document.getElementById("signup").disabled=true;
        document.getElementById("text").innerHTML = "please enter valid no";
    }
    else{
        var num1 =num.length;
        if(num1 == 10){
            ph.className= "success";
            document.getElementById("text").innerHTML= "";
        }
         else{
            ph.className="error";
            document.getElementById("signup").disabled=true;
            document.getElementById("text").innerHTML = "please enter valid no";
        }
    }
}

function validpass() {
    var pass1=pass1.value.length;
    if (pass1 >= 8 & pass1 <=16) {
        pass1.className = "success";
        document.getElementById("text").innerHTML="";

    }
    else {
        pass1.className="error";
        document.getElementById("signup").disabled=true;
        document.getElementById("text").innerHTML="Password length must be greater than 8 characters and not exceed than 16"
    }
}
function  validpassconform(){
    var pass=pass1.value;
    var passc=pass2.value;
    if (pass == passc){
        pass2.className="success"
        document.getElementById("text").innerHTML=""
        document.getElementById("signup").disabled=false
    }
    else{
        pass2.className="error"
        document.getElementById("signup").disabled=true
        document.getElementById("text").innerHTML="Passwords are not match"

      
    }
}
document.getElementById("signup").disabled=true;