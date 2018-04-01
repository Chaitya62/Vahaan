$(document).ready(function () {
const url=""
var regUser=`
<div class="card mt-4"> 
<div class="card-body">
<h5 class="card-title">Special title treatment</h5>
<p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
<a href="#" class="btn btn-primary">Puc</a>
<a href="#" class="btn btn-primary">Ticketing</a>
<a href="#" class="btn btn-primary">Toll</a>
</div>
</div>
`

$("#sample6").keypress(function(e){
    if(e.which===13){

        var regNo=$(e.target).val();

        
        // $.post(url,{'vehicle_id':getCookie('vehicle_id')},function(data,status){

        //     console.log(regNo);
        // })
    }
})

})