// App.js

document.addEventListener('DOMContentLoaded', function()
{
    console.log('index: DOM fully loaded and parsed');
});


function click_me(){
    element = document.getElementById("response_id");
    element.innerHTML = "Thank you very much for clicking"
}

