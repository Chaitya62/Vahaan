const url = "http://eed1c029.ngrok.io"

$(document).ready(function () {

$("#sample6").keypress(function(e){
    if(e.which===13){
        
        var regNo=$(e.target).val();
        
        $.post(url+"/get/user/",{'reg_no':regNo},function(data,status){
            data=JSON.parse(data)

            console.log(data);
            vault.set("vehicle_id",data.vehicle_id);
             var regUser = `
            <div class="card mt-4">
            <div class="card-body">
            <h5 class="card-title"><a href="${data}">${data.username}</a></h5>
            <p class="card-text"></p>
            <a href="#" class="btn btn-primary">Puc</a>
            <a href="#" class="btn btn-primary">Ticketing</a>
            <a href="#" class="btn btn-primary">Toll</a>
            </div>
            </div>
            `
            $("#regUserDiv").append(regUser);

        })

    }
})

})