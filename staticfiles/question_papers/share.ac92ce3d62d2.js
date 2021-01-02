const provideShare = document.getElementById("ask").addEventListener("click", sharefunc())
const appShare = document.getElementById("appShare").addEventListener('click', sharefunc("app"))
const paperShare = document.getElementById("paperShare").addEventListener('click', sharefunc)("paper")


function sharefunc() {
    let share = document.getElementById("share")
    var link
    var text
    // if (arg == "provider") {
    //     link = "http://questionpaper.herokuapp.com"
    //     text = "Share your questionpaper using the following link"
        
    // }
    console.log('clicked share');
    share.innerHTML = `
    <div id="appshare">
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

}
