function validateForm(event) {
  var result = [];

  result.push("Fullname: " + document.getElementById("fullname").value);

  var errors = [];
  let password1 = document.getElementById("password1").value;
  let password2 = document.getElementById("password2").value;

  if (password1 != password2) {
    errors.push("Passwords don't match");
  }

  if (
    !/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-_;:,.]).{8,20}$/.test(
      password1
    )
  ) {
    errors.push(
      "Password must be 8-20 characters, at least one uppercase, one lowercase letter, at least one digit and one special character."
    );
  }

  let message = "";
  if (errors.length > 0) {
    message = errors.join("\n");
  }
  var elem = document.getElementById("error_message");
  elem.className = "error";
  elem.innerText = message;
  if (errors.length == 0) {
    result.push("Password1: " + document.getElementById("password1").value);
    result.push("Password2: " + document.getElementById("password2").value);
  }

  var genderChosen = "";
  for (let gender of ["male", "female", "other"]) {
    if (document.getElementById("gender_" + gender).checked) {
      genderChosen = gender;
      break;
    }
  }
  if (genderChosen) {
    result.push("Gender: " + genderChosen);
  }

  var hobbies = [];
  for (let hobby of ["sports", "music", "games", "tv"]) {
    if (document.getElementById("hobby_" + hobby).checked) {
      hobbies.push(hobby);
    }
  }
  if (hobbies.length > 0) {
    result.push("Hobbies: " + hobbies.join(", "));
  }

  let mycountries = [];
  let countries = document.getElementById("country");
  for (let country of countries.options) {
    if (country.selected) {
      mycountries.push(country.label);
    }
  }
  if (mycountries) {
    result.push("Country: " + mycountries);
  }

  result.push(
    "height = " +
      (document.getElementById("id_number_input").value * 0.01).toFixed(2) +
      " m"
  );

  var txtCountry = document.getElementById("profession");
  var destination = txtCountry.value;

  if (destination) {
    result.push("Profession: " + destination);
  }

  var bday = document.getElementById("birthdate").value;
  if (bday) {
    result.push("Birthdate: " + bday);
  }

  var my_color = document.getElementById("myColor").value;
  if (my_color) {
    result.push("Favorite color: " + my_color);
  }

  var area_text = document.getElementById("id_message").value;
  text_lb = area_text.replace(/(?:\r\n|\r|\n)/g, "<br />");

  if (text_lb) {
    result.push("Message: " + text_lb);
  }

  document.getElementById("output").innerHTML = result.join("<br>");
  event.preventDefault();
  return false;
}
