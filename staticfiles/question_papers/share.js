// {% load static %}
const provideShare=document.getElementById("ask")
const appShare=document.getElementById("appShare")
const paperShare=document.getElementById("paperShare")


let share=document.getElementById("share")
function share(){
    if (provideShare) {
         link="http://questionpaper.herokuapp.com"
         text="Share your questionpaper using the following link"
        
    }
    html=`
    <div id="appshare" style="display: none;">
        <a class="social" href="https://www.facebook.com/sharer/sharer.php?u= ${link}"
            target="_blank"><img src="{%static 'question_papers/images/facebook.png'%}" alt="#"> Share on Facebook</a>
        <a class="social" href="https://api.whatsapp.com/send?text= ${text} ${link}
      " target="_blank"><img src="{%static 'question_papers/images/whatsapp.jpg'%}" alt="#">
            share on
            whatsapp</a>
        <a class="social" href="https://twitter.com/intent/tweet?text=https://questionpaper.herokuapp.com/ ,
            Awesome app to share question papers" target="_blank"><img
                src="{%static 'question_papers/images/twitter.jpg'%}" alt="#">
            share on
            twitter</a>
        <a class="social" href="mailto:?subject=Question Paper from QP&body=https://questionpaper.herokuapp.com/,
     Question Paper," target="_blank"><img src="{%static 'question_papers/images/mail.jpg'%}" alt="#"> share
            on mail</a>
        <a class="social" href="https://t.me/share/url?text=%s&url=https://questionpaper.herokuapp.com/ ,
            Awesome app to share question papers," target="_blank"><img
                src="{%static 'question_papers/images/telegram.jpg'%}" alt="#">
            share on
            telegram</a>
        <a class="social" href="https://www.linkedin.com/shareArticle?mini=true&title=Question Paper from QP&url=
    https://questionpaper.herokuapp.com/,
    Awesome app to share question papers," target="_blank"><img src="{%static 'question_papers/images/linkedin.jpg'%}"
                alt="#">
            share on
            linkedin</a>

    </div>`
    share.innerhtml=html
    }