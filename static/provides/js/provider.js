document.getElementById("id_paper_type").addEventListener("change", (e) => {
  let course_field = document.getElementById("id_course_name");
  let education = document.getElementById("id_education_type");
  let period = document.getElementById("id_period");

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

    for (let i = 0; i < period.options.length; i++) {
      if (
        period.options[i].text == "first" ||
        period.options[i].text == "second" ||
        period.options[i].text == "third"
      )
        period.options[i].hidden = false;
      else period.options[i].hidden = true;
    }
  } else {
    let displyStyle;
    if (window.matchMedia("(max-width: 600px").matches) {
      displyStyle = "block";
    } else {
      displyStyle = "flex";
    }

    course_field.parentNode.style.display = displyStyle;
    for (let i = 0; i < education.options.length; i++) {
      if (
        education.options[i].text == "SSLC" ||
        education.options[i].text == "PUC"
      )
        education.options[i].hidden = true;
      else education.options[i].hidden = false;
    }
    for (let i = 0; i < period.options.length; i++) {
      period.options[i].hidden = false;
    }
  }
});

// async function get_vehical_info() {
//   url = `?paper_type=university`;
//   selected_paper_type = document.getElementById("id_paper_type").value;
//   console.log(selected_paper_type);
//   // selected_type = document.getElementById('type').value
//   // selected_company = document.getElementById('company').value
//   // selected_name = document.getElementById('name').value
//   vehical_type = await fetch(
//     `${window.location.origin}/provide/provide_filter${url}`
//   )
//     .then((res) => res.json())
//     .then((data) => data);
//   console.log(vehical_type);
// }
// get_vehical_info();

async function  add_item(input,url,val){
  
  $.ajax({
    type: "POST",
    url: "/nouns/"+url,
    data: {
      $key: val,
      name: input,
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      action: "post",
    },
    success: function (json) {
      console.log(json);
      data={ value: String(json.instance.name), text: String(json.instance.name) }
      return data;
    },
    error: function (xhr, errmsg, err) {
      alert(`${input} already exist`);
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info 
      return null;
    },
  });
}
async function  add_governing_item(input,url,val){
  
  $.ajax({
    type: "POST",
    url: "/nouns/"+url,
    data: {
      education: val,
      name: input,
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      action: "post",
    },
    success: function (json) {
      console.log(json);
      data={ value: String(json.instance.name), text: String(json.instance.name) }
      return data;
    },
    error: function (xhr, errmsg, err) {
      alert(`${input} already exist`);
      console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info 
      return null;
    },
  });
}

// code for selecting by search
$(document).ready( function () {
  var $paper_type = $("#id_paper_type").selectize({
    sortField: "text",
  });

  var $education_type = $("#id_education_type").selectize({
    sortField: "text",
    create: async function (input, callback) {
      paper_type = $("#id_paper_type").val();
      // print( $("#id_paper_type"))
      if (!paper_type) {
        alert("Paper type is required");
      } else {
        data=await add_item(input,"create_eduation_type",paper_type)
        callback(data)
        return;
      
      }
      callback(null)
    },
  });
  var education_types = $education_type[0].selectize;

  // var data = {
  //   value: "item.title",
  //   text: "item.image",
  // };
  education_types.addOption({
    value: "title",
    text: "image",
  });
  // education_types.refreshOptions();

  var $governing_body = $("#id_governing_body").selectize({
    sortField: "text",
    create: async function (input, callback) {
      education_type = $("#id_education_type");
      education_type=education_type.val()
      console.log(education_type)
      if (!education_type) {
        alert("Paper type is required");
      } else {
        data=await add_governing_item(input,"create_governing_body",education_type)
        callback(data)
        return;
      
      }
      callback(null)
    },
  });
  var governing_bodys = $governing_body[0].selectize;

  var data = {
    value: "item.title",
    text: "item.image",
  };
  governing_bodys.addOption(data);
  // governing_bodys.refreshOptions();

  var $course_name = $("#id_course_name").selectize({
    sortField: "text",
    create: function (input, callback) {
      // console.log(input);
      callback({ value:input, text: input });
    },
  });
  var course_names = $course_name[0].selectize;

  var data = {
    value: "item.title",
    text: "item.image",
  };
  course_names.addOption(data);
  // course_names.refreshOptions();

  var $period = $("#id_period").selectize({
    sortField: "text",
    create: function (input, callback) {
      console.log(input);
      callback({ value: "hello", text: "hii" });
    },
  });
  var periods = $period[0].selectize;

  var data = {
    value: "item.title",
    text: "item.image",
  };
  periods.addOption(data);
  // periods.refreshOptions();

  var $subject_name = $("#id_subject_name").selectize({
    sortField: "text",
    create: function (input, callback) {
      console.log(input);
      callback({ value: "hello", text: "hii" });
    },
  });
  var subject_names = $subject_name[0].selectize;
 
  var data = {
    value: "item.title",
    text: "item.image",
  };
  subject_names.addOption(data);
  // subject_names.refreshOptions();
});
