
let selector_university = document.getElementById("university");
let selector_course = document.getElementById("course");
let selector_year = document.getElementById("year");
let selector_subject = document.getElementById("subject");

let select_first = document.getElementById("college");
let select_second = document.getElementById("university");
let select_third = document.getElementById("course");
let select_four = document.getElementById("year");
let select_college = document.getElementById("college");


let university;
let college;
let course;
let paperr;
let subject;
let year;
let examination;



let options = `<option>--select--</option>`;

function get_filter_first_option() {
  console.log("host "+window.location.href);
  console.log("You have changed the filter");
  console.log("value " + select_first.value);
  const value = select_first.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `http://127.0.0.1:8000/filter_first_option`;
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;

        let option = ` <option value="${college}" name="${college}">${college}</option>`;
        options += Option;
      }
      select_college.innerHTML = options;
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
}

function sel_First_Func() {
  const value = select_first.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `http://127.0.0.1:8000/json-${value}`;
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;

        let option = document.createElement("option");
        option.text = university;
        option.setAttribute("name", "university");
        option.value = university;
        selector_university.appendChild(option);
        university = "";
      }
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
}

function sel_Sec_Func() {
  const value1 = select_first.value;
  const value2 = select_second.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `http://127.0.0.1:8000/json-${value1}/${value2}`.replace(" ", "");
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;

        let option = document.createElement("option");
        option.text = course;
        option.setAttribute("name", "course");
        option.value = course;
        selector_course.appendChild(option);
        course = "";
      }
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
}

function sel_Third_Func() {
  const value1 = select_first.value;
  const value2 = select_second.value;
  const value3 = select_third.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `http://127.0.0.1:8000/json-${value1}/${value2}/${value3}`;
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;

        let option = document.createElement("option");
        option.text = year;
        option.setAttribute("name", "year");
        option.value = year;
        selector_year.appendChild(option);
        year = "";
      }
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
}

function sel_Four_Func() {
  const value1 = select_first.value;
  const value2 = select_second.value;
  const value3 = select_third.value;
  const value4 = select_four.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url =
    `http://127.0.0.1:8000/json-${value1}/${value2}/${value3}/${value4}`.replace(
      " ",
      ""
    );
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;

        let option = document.createElement("option");
        option.text = subject;
        option.setAttribute("name", "subject");
        option.value = subject;
        selector_subject.appendChild(option);
        subject = "";
      }
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
}
