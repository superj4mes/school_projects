function handleSubmit(event) {
  event.preventDefault();
  return false;
}

function reset_graph() {
  text.splice(0, text.length);
  results.splice(0, results.length);
  document.getElementById("output").value = "";
}

const CHART = document.getElementById("lineChart").getContext("2d");
let text = [];
let results = [];

let lineChart = new Chart(CHART, {
  type: "line",
  data: {
    labels: text,
    datasets: [
      {
        label: "Function calculator",
        fill: false,
        lineTension: 0.4,
        borderColor: "#0000FF",
        borderWidth: 1.5,
        data: results,
      },
    ],
  },
});

function calc() {
  reset_graph();

  let func = document.getElementById("func_id").value;
  let x = parseInt(document.getElementById("start_x").value);
  let end = parseInt(document.getElementById("end_x").value);
  let step = parseFloat(document.getElementById("step_x").value);

  for (; x <= end; x = x + step) {
    with (Math) {
      try {
        var res = eval(func);
        results.push(res);
        text.push(x);

        //document.getElementById("output").innerHTML += `f(${x.toFixed(2)}) = ${res} ${"<br>"}`;
        output_field = `f(${x.toFixed(1)}) = ${res.toFixed(5)} ${"<br>"}`;
        document.getElementById("output").innerHTML += output_field;
      } catch (e) {
        alert(e);
        break;
      }
    }
  }

  lineChart.update();
}
