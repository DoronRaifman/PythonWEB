// App.js

function calculate(){
    var ids = ['x', 'y'];
    var inputs = { };
    for (i=0;i < ids.length;i++) {
        inputs[ids[i]] = document.getElementById(ids[i]).value;
    }
    my_ajax_get(inputs, 'GET', '/get_result', handle_result);
}

function handle_result(result){
    console.log(result);
    keys = Object.keys(result);
    for(i=0;i < keys.length;i++) {
        key = keys[i];
        document.getElementById(key).value = result[key];
    }
}

function my_ajax_get(inputs, get_post, url, callback) {
    if (get_post == 'GET'){
            my_inputs = inputs;
        }
    else if (get_post == 'POST') {
            my_inputs = JSON.stringify(inputs);
        }
    else {
        alert('Bad AJAX call');
        return;
    }
    $.ajax({
        type: get_post,
        url: url,
        data: my_inputs,
    }).done(function (result) {
        callback(result);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR, textStatus, errorThrown);
    })
}


