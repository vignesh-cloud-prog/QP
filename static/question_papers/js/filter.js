// filter section
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

const base_url = window.location.origin;

function get_filter_first_option() {
  let options = `<option>--select--</option>`;

  const value = select_first.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `${base_url}/filter_first_option`;
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        college = obj[key].fields.education_type;

        let option = ` <option value="${college}" name="${college}">${college}</option>`;
        options += option;
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
  let options = `<option>--select--</option>`;

  const value = select_first.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `${base_url}/json-${value}`;

  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);

      let str;
      for (key in obj) {
        university = obj[key].fields.governing_body;

        let option = ` <option value="${university}" name="${university}">${university}</option>`;
        options += option;
      }
      selector_university.innerHTML = options;
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
}

function sel_Sec_Func() {
  let options = `<option>--select--</option>`;

  const value1 = select_first.value;
  const value2 = select_second.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `${base_url}/json-${value1}/${value2}`.replace(" ", "");

  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);

      let str;
      for (key in obj) {
        course = obj[key].fields.course_name;

        let option = ` <option value="${course}" name="${course}">${course}</option>`;
        options += option;
      }
      selector_course.innerHTML = options;
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
}

function sel_Third_Func() {
  let options = `<option>--select--</option>`;
  console.log("You have changed the filter");
  console.log("value " + select_first.value);
  const value1 = select_first.value;
  const value2 = select_second.value;
  const value3 = select_third.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `${base_url}/json-${value1}/${value2}/${value3}`;
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        year = obj[key].fields.period;

        let option = ` <option value="${year}" name="${year}">${year}</option>`;
        options += option;
      }
      selector_year.innerHTML = options;
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
}

function sel_Four_Func() {
  let options = `<option>--select--</option>`;

  const value1 = select_first.value;
  const value2 = select_second.value;
  const value3 = select_third.value;
  const value4 = select_four.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `${base_url}/json-${value1}/${value2}/${value3}/${value4}`.replace(
    " ",
    ""
  );

  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        subject = obj[key].fields.subject_name;

        let option = ` <option value="${subject}" name="${subject}">${subject}</option>`;
        options += option;
      }
      selector_subject.innerHTML = options;
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
}
// end of filter section
