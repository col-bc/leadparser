function approveAll() {
  // get all the checkboxes
  var checkboxes = document.querySelectorAll("input[type=checkbox]");
  // loop over them
  checkboxes.forEach(function (checkbox) {
    // check the checkbox
    checkbox.checked = true;
  });
}
