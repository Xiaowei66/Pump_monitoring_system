

var vt_chart;
$(document).ready(function () {
   vt_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'vtChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The VIBRATION_TANGENTIAL chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "VIBRATION_TANGENTIAL",
           data: [0]
       }]
   });
});

var vr_chart;
$(document).ready(function () {
   vr_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'vrChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The VIBRATION_RADIAL chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "VIBRATION_RADIAL",
           data: [0]
       }]
   });
});

var va_chart;
$(document).ready(function () {
   va_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'vaChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The VIBRATION_AXIAL chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "VIBRATION_AXIAL",
           data: [0]
       }]
   });
});

var output_chart;
$(document).ready(function () {
   output_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'outputChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The output chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "output",
           data: [0]
       }]
   });
});

var speed_chart;
$(document).ready(function () {
   speed_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'speedChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The speed chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "speed",
           data: [0]
       }]
   });
});

var temperature_char;
$(document).ready(function () {
   temperature_char = new Highcharts.Chart({
      chart: {
        renderTo: 'tempChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The temperature chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "temperature",
           data: [0]
       }]
   });
});

var pump_temperature = [];
var pump_power = [];
var speed = [];
var va = [];
var vr = [];
var vt = [];


function setData() {
    try {
        $.get("http://127.0.0.1:7500/states", function (data) {

            // console.log(data);

            // var res = data[0];
            for (i = 0; i < data.length; i ++) {
                var res = data[i];
                // console.log(res.id);
                if (res.id === parseInt($("#current_pump").val())) {
                    $("#pump_id").html(res.id);
                    $("#pump_address").html(res.address);
                    $("#pump_avibration").html(res.axial_vibration);
                    $("#pump_power").html(res.power);
                    $("#pump_rvibration").html(res.radial_vibration);
                    $("#pump_speed").html(res.speed);
                    $("#pump_tvibration").html(res.tangential_vibration);
                    $("#pump_temperature").html(res.temperature);

                    pump_temperature = remove_data(pump_temperature);
                    pump_power = remove_data(pump_power);
                    speed = remove_data(speed);
                    va = remove_data(va);
                    vr = remove_data(vr);
                    vt = remove_data(vt);

                    // console.log(pump_temperature.length);

                    pump_temperature.push(res.temperature);
                    pump_power.push(res.power);
                    speed.push(res.speed);
                    va.push(res.axial_vibration);
                    vr.push(res.radial_vibration);
                    vt.push(res.tangential_vibration);
                }

            }

            // which means the pump states is error
            if (parseInt(res.error) === -1) {
                $.post("http://127.0.0.1:7500/message",
                    {"send_from":"0450539776", "send_to":"0413164212", "content":"Please go to check pump located at: " + res.address
                            + ". Its temperature is abnormal: " + res.temperature}, function (data, status) {
                    console.log(data, status);
                });
            }

            // temperature_char.chart.renderTo = "";
            temperature_char.series[0].setData(pump_temperature);
            output_chart.series[0].setData(pump_power);
            speed_chart.series[0].setData(speed);
            va_chart.series[0].setData(va);
            vr_chart.series[0].setData(vr);
            vt_chart.series[0].setData(vt);


        }).fail(function () {
            clearInterval(t);
        });
    } catch (e) {
        alert(e);
    }
}
var t = setInterval(setData, 1000);

$("#logout").show();

function remove_data(data) {
    var res = data;
    if (data.length > 30) {
        for (var i = 0; i <= data.length - 30; i ++) {
            res.shift();
        }
    }

    return res;
}

function change(id) {
    $("#" + $("#current_pump").val()).parent()[0].className = "";
    $("#" + id).parent()[0].className = "active";

    $("#current_pump").val(id);

var vt_chart;
$(document).ready(function () {
   vt_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'vtChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The VIBRATION_TANGENTIAL chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "VIBRATION_TANGENTIAL",
           data: [0]
       }]
   });
});

var vr_chart;
$(document).ready(function () {
   vr_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'vrChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The VIBRATION_RADIAL chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "VIBRATION_RADIAL",
           data: [0]
       }]
   });
});

var va_chart;
$(document).ready(function () {
   va_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'vaChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The VIBRATION_AXIAL chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "VIBRATION_AXIAL",
           data: [0]
       }]
   });
});

var output_chart;
$(document).ready(function () {
   output_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'outputChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The output chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "output",
           data: [0]
       }]
   });
});

var speed_chart;
$(document).ready(function () {
   speed_chart = new Highcharts.Chart({
      chart: {
        renderTo: 'speedChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The speed chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "speed",
           data: [0]
       }]
   });
});

var temperature_char;
$(document).ready(function () {
   temperature_char = new Highcharts.Chart({
      chart: {
        renderTo: 'tempChart',
        plotBackgroundColor: null,
        plotBorderWidth: null,
        defaultSeriesType: 'line'
      }, title: {
         text: "The temperature chart"
      }, xAxis: {
          categories: [],
           labels: {
              rotation: -45,
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
          line: {
              dataLabels: {
                  enabled: true
              },
              enableMouseTracking: true
          }
       }, series: [{
          name: "temperature",
           data: [0]
       }]
   });
});

var pump_temperature = [];
var pump_power = [];
var speed = [];
var va = [];
var vr = [];
var vt = [];


function setData() {
    try {
        $.get("http://127.0.0.1:7500/states", function (data) {

            // console.log(data);

            // var res = data[0];
            for (i = 0; i < data.length; i ++) {
                var res = data[i];

                // console.log(res.id);

                if (res.id === parseInt($("#current_pump").val())) {

                    $("#pump_id").html(res.id);
                    $("#pump_address").html(res.address);
                    $("#pump_avibration").html(res.axial_vibration);
                    $("#pump_power").html(res.power);
                    $("#pump_rvibration").html(res.radial_vibration);
                    $("#pump_speed").html(res.speed);
                    $("#pump_tvibration").html(res.tangential_vibration);
                    $("#pump_temperature").html(res.temperature);

                    pump_temperature = remove_data(pump_temperature);
                    pump_power = remove_data(pump_power);
                    speed = remove_data(speed);
                    va = remove_data(va);
                    vr = remove_data(vr);
                    vt = remove_data(vt);

                    // console.log(pump_temperature.length);

                    pump_temperature.push(res.temperature);
                    pump_power.push(res.power);
                    speed.push(res.speed);
                    va.push(res.axial_vibration);
                    vr.push(res.radial_vibration);
                    vt.push(res.tangential_vibration);
                }

            }

            if (parseInt(res.temperature) >= 40 || parseInt(res.speed) >= 1550) {
                $.post("http://127.0.0.1:7500/message",
                    {"send_from":"61450539776", "send_to":"all", "content":"Please go to check pump located at: " + res.address
                            + ". Its temperature is abnormal: " + res.temperature}, function (data, status) {
                    console.log(data, status);
                });
            }

            // temperature_char.chart.renderTo = "";
            temperature_char.series[0].setData(pump_temperature);
            output_chart.series[0].setData(pump_power);
            speed_chart.series[0].setData(speed);
            va_chart.series[0].setData(va);
            vr_chart.series[0].setData(vr);
            vt_chart.series[0].setData(vt);


        }).fail(function () {
            clearInterval(t);
        });
    } catch (e) {
        alert(e);
    }
}
var t = setInterval(setData, 1000);

$("#logout").show();

function remove_data(data) {
    var res = data;
    if (data.length > 30) {
        for (var i = 0; i <= data.length - 30; i ++) {
            res.shift();
        }
    }

    return res;
}

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

    $("#pump_id").html(id);

    pump_temperature = [];
    pump_power = [];
    speed = [];
    va = [];
    vr = [];
    vt = [];

}