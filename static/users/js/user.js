function ReSendOTP(username, mess_id) {

    mess = document.getElementById(mess_id);
    mess.innerText = "Sending...";
   
    fetch(`/user/resendOTP/${username}`).then((res)=>res.json()).then(data=>{mess.innerText = data.msg})
    
}