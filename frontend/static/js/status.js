$("#logout").show();

function get_status() {
    try {
        $.get('http://127.0.0.1:8500/status', function (data, status) {
            var html = "";
            for (i = 0; i < data.length; i ++) {
                var status = "success";
                var html_status = "Normal";
                if (data[i].error === 0) {
                    status = "warning";
                    html_status = "Warning"
                } else if (data[i].error === -1) {
                    status = "danger";
                    html_status = "Abnormal"
                }

                html += "<tr class=\"" + status + "\">";
                html += "<td> <a  href=\"/" + data[i].id + "\">Pump " + data[i].id + "</a></td>";
                html += "<td>" + data[i].address + "</td>";
                html += "<td>" + html_status + "</td>";
                html += "</tr>";

            }

            $("#pumps").html(html);

        }).fail(function () {
                clearInterval(t);
        });
    }catch (e) {

    }
}
get_status();
var t = setInterval(get_status, 2000);