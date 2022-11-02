document.addEventListener('DOMContentLoaded', function()
{
    console.log('index: DOM fully loaded and parsed');
});


function login(){
    var user_name = document.getElementById('user_name').value;
    var password = document.getElementById('password').value;
    var remember = document.getElementById('remember').value;
    console.log('login: user:'+user_name+', pwd:'+password);
    var data = {'user_name': user_name, 'password': password, 'remember': remember};
    var url = '/login';
    my_ajax_get(data, 'GET', url, handle_login_result);
}

function handle_login_result(result){
    // console.log(result);
    message = result['message'];
    if(result['is_ok']){
        console.log('Result:'+message);
        delete result['message'];
        delete result['is_ok'];
        user_id = result['user_id'];
        // Todo: take result data and pass as parameters
        var url = '/customers/' + user_id + '/';
        window.location.replace(url);
    }
    else
        alert(message);
}

function my_ajax_get(inputs, get_post, url, callback) {
    if (get_post == 'GET'){
            var my_inputs = inputs;
        }
    else if (get_post == 'POST') {
            var my_inputs = JSON.stringify(inputs);
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
