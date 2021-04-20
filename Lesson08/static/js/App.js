// App.js
document.addEventListener('DOMContentLoaded', function()
{
    console.log('index: DOM fully loaded and parsed');
});


function call_item(user_id, item_id){
    console.log('goto item:' + item_id);
    var url = "/get_data?user_id=" + user_id + "&papa_id=" + item_id;
    window.location.href = url;
}

function go_up(){
    console.log('go up');
    grandpa_id = document.getElementById("grandpa_id").innerHTML;
    user_id = document.getElementById("user_id").value
    call_item(user_id, grandpa_id)
}

function login() {
    var user_name_1 = document.getElementById("user_name").value;
    $.get(
        '/login',
        {user_name: user_name_1},
        function (data) {
            console.log(data);
            user_id1 = data['idusers'];
            user_id1 = parseInt(user_id1);
            if (user_id1 > 0){
                user_name = user_name_1;
                user_id = user_id1;
                call_item(user_id, 0);
            }
            else {
                alert('Bad user name');
            }
            document.getElementById("Version").innerHTML = " " + data;
        },
        'json');
}
