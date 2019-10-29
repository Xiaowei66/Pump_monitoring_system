$("#logout").show();
function predirection() {
    $("#pre").html("");
    try {
        $.post('http://127.0.0.1:9999/learning/', function (data) {

            // console.log(data);

            for (var i  = 0; i < data.length; i ++ ){
                var res = data[i];
                var status = "success";
                var html = "";
                if (res.probability >= 20 && res.probability < 50) {
                    status = "warning";
                } else if (res.probability >= 50) {
                    status = "danger";
                }

                html += "<tr class=\"" + status + "\">";
                html += "<td> <a  href=\"history/" + data[i].id + "\">Pump " + data[i].id + "</a></td>";
                html += "<td>" + res.address + "</td>";
                html += "<td>" + res.probability + "%</td>";
                html += "</tr>";
                $("#pre").append(html);
            }
        });
    } catch (e) {
        clearInterval(t);
    }
}


predirection();
var t = setInterval(predirection, 5000);