var pump_data = [];
var type =["Normal", "Warning", "Accident"];
var char;
$(document).ready(function () {
   char = new Highcharts.Chart({
      chart: {
        renderTo: 'tempChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'column'
      }, title: {
         text: "The data analysis"
      }, xAxis: {
          categories: ["The status"],
           lineWidth: 1,
           labels: {
              rotation: 0,
               align: 'right',
           }
       }, yAxis: {
          title: {
              text: "DATA"
          }
       }, tooltip: {
          enabled: true,
            formatter: function() {
                return '<b>' + this.x + '</b><br/>' + this.series.name + ': ' + Highcharts.numberFormat(this.y, 1);
            }
       }, plotOptions: {
          column: {
              dataLabels: {
                  enabled: true,
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "Normal",
           data: [0],
           color:"blue"
       }, {
          name: "Warning",
           data:[0],
           color: "orange",
       }, {
          name: "Abnormal",
           data: [0],
           color: "red"
       }]
   });
});


function setData() {
    try {
        $.get("http://127.0.0.1:7500/data",{"pump": $("#current_pump").val()}, function (data) {

            pump_data = [];
            var wan = [];
            var ab = [];
            var res = data[0];
            pump_data.push(res.normal);
            wan.push(res.warning);
            ab.push(res.accident);

            console.log(pump_data);
            char.series[0].setData(pump_data);
            char.series[1].setData(wan);
            char.series[2].setData(ab);


        }).fail(function () {
            clearInterval(t);
        });
    } catch (e) {
        alert(e);
    }
}

var t = setInterval(setData, 1000);

$("#logout").show();

function change(id) {
    $("#" + $("#current_pump").val()).parent()[0].className = "";
    $("#" + id).parent()[0].className = "active";

    $("#current_pump").val(id);

    $("#pump_id").html(id);

    pump_temperature = [];
    pump_power = [];
    speed = [];
    va = [];
    vr = [];
    vt = [];

}