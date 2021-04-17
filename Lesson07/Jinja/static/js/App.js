// App.js

document.addEventListener('DOMContentLoaded', function()
{
    console.log('index: DOM fully loaded and parsed');
    $.get(
        '/version',
        {'stam': 1},
        function (data) {
            console.log(data);
            document.getElementById("Version").innerHTML = '' + data;
        },
        'html');
});


function get_radio(group_name){
    var elements = document.getElementsByName(group_name);
    var val = 0;
    for (var i = 0; i < elements.length; i++){
        var elem = elements[i];
        if(elem.checked) {
            val = elem.value;
            break;
        }
    }
    return(val);
}


function rerun_execute(elem){
    project_id = document.getElementById("project_id").value;
    couple_id = document.getElementById("couple_id").value;
    days_count = document.getElementById("days_count").value;
    Project_Couple = get_radio("Project_Couple");

    var inputs = {
        project_id:project_id, couple_id:couple_id,
        days_count:days_count, Project_Couple:Project_Couple};
    console.log("rerun_execute:");
    console.log(inputs)

    $.get(
        '/rerun',
        inputs,
        function (data) {
            console.log(data);
        },
        'html');
}

