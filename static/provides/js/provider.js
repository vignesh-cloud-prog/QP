document.getElementById("id_paper_type").addEventListener("change", (e) => {
  let course_field = document.getElementById("id_course_name");
  let education = document.getElementById("id_education_type");

  if (e.target.value == "board") {
    course_field.parentNode.style.display = "none";

    for (let i = 0; i < education.options.length; i++) {
      if (
        education.options[i].text == "SSLC" ||
        education.options[i].text == "PUC"
      )
        education.options[i].hidden = false;
      else education.options[i].hidden = true;
    }
  } else {
    course_field.parentNode.style.display = "block";
    for (let i = 0; i < education.options.length; i++) {
      if (
        education.options[i].text == "SSLC" ||
        education.options[i].text == "PUC"
      )
        education.options[i].hidden = true;
      else education.options[i].hidden = false;
    }
  }
});
