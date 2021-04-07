// App.js
function get_data(){
    var ids = ['fname', 'lname', 'age'];
    var inputs = { };
    for (i=0;i < ids.length;i++) {
        inputs[ids[i]] = document.getElementById(ids[i]).value;
    }
    my_ajax1(inputs);
}

function handle_result(result){
    console.log(result);
    keys = Object.keys(result);
    for(i=0;i < keys.length;i++) {
        key = keys[i];
        document.getElementById(key).value = result[key];
    }
}

function my_ajax1(inputs){
    $.get(
        '/get_result',
        inputs,
        function (result) {
            handle_result(result);
        }, "json");
}

function my_ajax2(inputs) {
    $.ajax({
        type: 'GET',
        url: '/get_result',
        data: inputs,
    }).done(function (result) {
        handle_result(result);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR, textStatus, errorThrown);
    })
}

function my_ajax3(inputs) {
    $.ajax({
        type: 'POST',
        url: '/get_result',
        data: JSON.stringify(inputs),
    }).done(function (result) {
        handle_result(result);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR, textStatus, errorThrown);
    })
}

