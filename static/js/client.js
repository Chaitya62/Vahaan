$(document).ready(function () {
    const url = "http://localhost:8000/puc/get/"
    $('#reg_number').html(getCookie('reg_no'))

    $.post(url, { 'vehicle_id': getCookie('vehicle_id') }, function (d, status) {
        data = JSON.parse(d);

        var pucList = `
    <li class="mdl-list__item mdl-list__item--two-line">
    <span class="mdl-list__item-primary-content">
    
    <span>Next Renewal PUC Date</span>
  
    </span>
    <span class="mdl-list__item-secondary-content">
    ${new Date(data.startDate).toDateString()}
    </span>
    </li>`

        $("#pucList").append(pucList);
    })

    $.get("/view_toll/"+getCookie('vehicle_id')+"/",function(data,status){

        tolls=JSON.parse(data);
        console.log(tolls);

/*         [
            {
                "toll": {
                    "name": "Ankit",
                    "location": "Mumbai",
                    "amount_vehicle_car": 100,
                    "amount_vehicle_truck": 200,
                    "amount_vehicle_lcv": 300,
                    "amount_vehicle_3axel": 400,
                    "amount_vehicle_4to6axel": 500,
                    "amount_vehicle_7axel": 600,
                    "amount_vehicle_hcm": 700
                },
                "vehicle": 1,
                "amount": 100,
                "date": "2018-04-18",
                "consumed": false
            }

        ] */

       

        function getTemplate(ticket){
             var vew = '';

        if(getCookie('isAdmin') === 'true'){
            var vew = `<a href="/consume/${ticket.toll.id}" class="btn btn-primary" style="position: relative;right:0px;">Consume</a>`;
        }
            
            return ` 
            <li class="mdl-list__item">
            <div class="card mt-4" style="width:100%">
            <div class="card-body">
            <h5 class="card-title">
            ${ticket.toll.name}
            </h5>
            <p class="card-text">
            ${ticket.toll.location}
            </p>
            <p class="card-text">
            ${ticket.amount} Rs.
            </p>
            <p class="card-text">
            ${ticket.date}
            </p>
            ${vew}
            </div>
            </div>
            </li>`
        }

        tolls.forEach(ticket => {
            $("#tollList").append(getTemplate(ticket));
        });
    })

});

function getCookie(cname) {
    // return 1;
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