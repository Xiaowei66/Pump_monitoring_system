$("#login").click(function () {
    username = $("#username").val();
    password = $("#password").val();

    if (username === "") {
        alert("Please enter username");
    }
    if (username === "") {
        alert("Please enter password");
    }

    $.getJSON("http://127.0.0.1:7700/login/", {"username": username, "password": password}, function (data, status) {
        if (status === "success") {
            window.localStorage.setItem("token", data.token);
            $.getJSON("/take_token", {"token": window.localStorage.getItem("token")});
            $(location).attr('href', "/");

            $("#login_base").hide();
            $("#logout").show();

        }

    }).fail(function (res) {
        alert(res.responseJSON.message);
    });
});