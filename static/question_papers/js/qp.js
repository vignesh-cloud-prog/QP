filter_open = document.getElementById("filter-btn");
filter_items = document.getElementById("filter_items");

close_filterItems = document.getElementById("close_filterItems");
// select_university=document.getElementById("university")

// select_first=document.getElementById("college")

let user_menu = document.getElementById("user_menu");
let user = document.getElementById("user");
function open_filter() {
  console.log("clicked filter button");
  get_filter_first_option();
  filter_items.style.display = "flex";
}
function close_filter() {
  console.log("clicked close filter button");
  filter_items.style.display = "none";
}

document.getElementById("user").addEventListener("click", () => {
  user_menu.style.display = "flex";
  user.classList.add("user_absolute");
});
document.getElementById("close_menu").addEventListener("click", () => {
  user.classList.remove("user_absolute");
  user_menu.style.display = "none";
});

navitems = document.getElementById("navitems");
function display_menu() {
  navitems.style.display = "flex";
}

setTimeout(() => {
  msg_box = document.getElementById("msg_box");
  if (msg_box) {
    msg_box.style.display = "none";
  }
}, 10000);

document.addEventListener('DOMContentLoaded', function() {
  let hour = new Date().getHours();
  let wish=(`Good ${hour < 12 && "Morning" || hour < 18 && "Afternoon" || "Evening"}`)
  document.getElementById("timeBasedGreet").innerHTML=wish
}, false);

