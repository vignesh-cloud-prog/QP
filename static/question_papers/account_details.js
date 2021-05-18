function edit_profile() 
{
    console.log("you requested to edit profile");
    document.getElementById("username").contentEditable="true";
    document.getElementById("userbio").contentEditable="true";
    document.getElementById("usercollege").contentEditable="true";
    document.getElementById("profile_photo_input").style.display="inline-block";
    
}
document.getElementById("edit_profile").addEventListener("click",edit_profile())
let editable=document.getElementsByClassName("editable");



function post_update_profile(){
    let username=document.getElementById("username").value
    let bio=document.getElementById("userbio").value
    let college=document.getElementById("usercollege").value
    let pic=document.getElementById("profile_photo_input").value
    let url="http://127.0.0.1:8000/profile/"
    url=url;
    data=`{"username":${username},"bio":${bio},"pic":${pic},"college":${college}}`
    params={
        method='post',
        headers:{
            'Content-Type':'application/json'
        },
        body:data
    }
    fetch(url,params).then(response=>response.json())
    .then(data=>console.log(data))
}