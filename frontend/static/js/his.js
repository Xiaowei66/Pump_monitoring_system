var pump_temperature = [];
var pump_power = [];
var speed = [];
var va = [];
var vr = [];
var vt = [];
var time =[];

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

function setData() {
    try {
        $.get("http://127.0.0.1:7800/history/", {"pump": $("#current_pump").val()} ,function (data) {
            // var res = data[0];

            // console.log(data.length);

            for (var i = 0; i < data.length; i ++ ){
                var res = data[i];

                pump_temperature.push(res.temperature);
                pump_power.push(res.power);
                speed.push(res.speed);
                va.push(res.axial_vibration);
                vr.push(res.radial_vibration);
                vt.push(res.tangential_vibration);
                time.push(res.time);
            }

            temperature_char.xAxis[0].setCategories(time);
            temperature_char.series[0].setData(pump_temperature);

            output_chart.xAxis[0].setCategories(time);
            output_chart.series[0].setData(pump_power);

            speed_chart.xAxis[0].setCategories(time);
            speed_chart.series[0].setData(speed);

            va_chart.xAxis[0].setCategories(time);
            va_chart.series[0].setData(va);

            vr_chart.xAxis[0].setCategories(time);
            vr_chart.series[0].setData(vr);

            vt_chart.xAxis[0].setCategories(time);
            vt_chart.series[0].setData(vt);

        }).fail(function () {
            clearInterval(t);
        });
    } catch (e) {
        alert(e);
    }
}
//var t = setInterval(setData, 1000);

setData();


$("#search").click( function () {
        // just clear the data
        pump_temperature = [];
        pump_power = [];
        speed = [];
        va = [];
        vr = [];
        vt = [];
        time = [];
        try {

            $.post('http://127.0.0.1:7800/history/', {"date": $("#searchdata").val(), "pump": $("#current_pump").val()}, function (data, status) {
                for (var i = 0; i < data.length; i ++ ){
                    var res = data[i];
                    // console.log(res)
                    pump_temperature.push(res.temperature);
                    pump_power.push(res.power);
                    speed.push(res.speed);
                    va.push(res.axial_vibration);
                    vr.push(res.radial_vibration);
                    vt.push(res.tangential_vibration);
                    time.push(res.time);

                }

                temperature_char.xAxis[0].setCategories(time);
                temperature_char.series[0].setData(pump_temperature);

                output_chart.xAxis[0].setCategories(time);
                output_chart.series[0].setData(pump_power);

                speed_chart.xAxis[0].setCategories(time);
                speed_chart.series[0].setData(speed);

                va_chart.xAxis[0].setCategories(time);
                va_chart.series[0].setData(va);

                vr_chart.xAxis[0].setCategories(time);
                vr_chart.series[0].setData(vr);

                vt_chart.xAxis[0].setCategories(time);
                vt_chart.series[0].setData(vt);
            })

        } catch (e) {

        }
    });

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

    setData();

}