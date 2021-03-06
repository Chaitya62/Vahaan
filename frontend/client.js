const url = "http://eed1c029.ngrok.io"

$(document).ready(function () {
    

    $.post(url+"/puc/get/", { 'vehicle_id': getCookie('vehicle_id') }, function (d, status) {
        data = JSON.parse(d);
        console.log(data)
        var pucList = `
    <li class="mdl-list__item mdl-list__item--two-line">
    <span class="mdl-list__item-primary-content">
    
    <span>Next pending PUC date</span>
  
    </span>
    <span class="mdl-list__item-secondary-content">
    ${new Date(data.startDate).toDateString()}
    </span>
    </li>`

        $("#pucList").append(pucList);
    })
});

function getCookie(cname) {
    return 1;
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}