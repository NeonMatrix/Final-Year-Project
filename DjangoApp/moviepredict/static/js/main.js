function addActor() {
    actorHtml = '<div class="form-row m-b-55">'+
    '<div class="name">Actor 1</div>'+
    '<div class="value">'+
        '<div class="row row-space">'+
            '<div class="col-1">'+
                '<div class="input-group-desc">'+
                    '<input class="input--style-5" type="text" name="actor[]">'+
                    '<label class="label--desc">Actor name</label>'+
                '</div>'+
            '</div>'+
        '</div>'+
    '</div>'+
'</div>';
    document.getElementById("actor_fields").appendChild(actorHtml);
   }