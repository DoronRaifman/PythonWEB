// App.js

document.addEventListener('DOMContentLoaded', function()
{
    console.log('index: Items DOM fully loaded and parsed');

    $.get(
    '/version',
    {},
    function (data) {
        console.log(data);
        document.getElementById("Version").innerHTML = " " + data;
    },
    'html');
    update_user_info();
});


