function calculateResult() {
    var display = document.getElementsByName("display")[0];
    var result = display.value;
  
    try {
      var output = eval(result);
      display.value = output;
    } catch (error) {
      display.value = "Error";
    }
  }
  