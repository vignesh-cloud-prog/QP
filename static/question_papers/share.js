
function sharefunc(link,message) {
    document.getElementById("close_menu").click();
    // profile.style.display="none";
    share=document.getElementById("appshare");
    share.style.display="grid";

    let facebook_url=`https://www.facebook.com/sharer/sharer.php?u=${link}`;
    let whatsapp_url=`https://api.whatsapp.com/send?text=${link}  ${message}`;
    let twitter_url=`https://twitter.com/intent/tweet?text=${link} , ${message}`;
    let mail_url=`mailto:?subject=QP Web Info QP&body=${link} , ${message}`;
    let telegram_url=`https://t.me/share/url?text=${link}&url=${message}`;
    let linkedlin_url=`https://www.linkedin.com/shareArticle?mini=true&title=${message}&url=${link}`

    document.getElementById("facebook").href=facebook_url;
    document.getElementById("whatsapp").href=whatsapp_url;
    document.getElementById("mail").href=mail_url;
    document.getElementById("twitter").href=twitter_url;
    document.getElementById("telegram").href=telegram_url;
    document.getElementById("linkedin").href=linkedlin_url;
    document.getElementById("link_text").innerText=link;

}
