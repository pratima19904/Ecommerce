// console.log("this is working")
// var x = "hello";
// var x = 67;
// let y = 98;
// let y = 89;
// alert(x);
// var x;
// for(x=0;x<=5;x++){
//     console.log(x);
// }
function validateform(){
    x=document.forms["myform"]["email"].value;
    if(x==""){
        document.getElementById('email').placeholder = "enter your email";
        document.getElementById('email').style.border = "2px solid red";
        var x =document.getElementById('valid');
        x.innerHTML = "*enter`- your email";
        x.style.color = "red";
    
        return false;

    }
        
    
}
