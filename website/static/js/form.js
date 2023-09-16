// Displays/disables form with provided ID;
function displayForm(form, x) {
    var form = document.getElementById(form);
    if (x) {
        form.style = "display: block; z-index: 999; position: fixed;";
    } else {
        form.style = "display: none;"
    }
}

console.log("Javascript loaded! LOLZ")