// Hanoi.js
document.addEventListener('DOMContentLoaded', function()
{
    console.log('index: DOM fully loaded and parsed');
    init_start_towers();
    display_towers();
    var timer = setInterval(run_timer, 200);
});

var tower_names = ['orig', 'helper', 'dest'];
var towers = { };
var n = 5;

function init_start_towers() {
    // top level is towers dict
    n = parseInt(document.getElementById("n").value);
    towers = {};
    var towers_count = tower_names.length;
    for (i = 0; i < towers_count; i++) {
        var tower_rings = [];
        var tower_name = tower_names[i];
        towers[tower_name] = tower_rings;
    }
    var src_tower_rings = towers[tower_names[0]];
    for (i = 0; i < n; i++) {
        var width = n - i + 2;
        src_tower_rings.push(width);
    }
}

var is_running = false;
var step_index = 0;
var tower_move_states = [];

function start() {
    stop();
    is_running = false;
    init_start_towers();
    display_towers();
    tower_move_states = [];
    tower_move_states.push(clone_object(towers));
    hanoi(n, tower_names[0], tower_names[1], tower_names[2]);
    step_index = 0;
    is_running = true;
}

function stop(){
    is_running = false;
}

function run_timer(){
    if (is_running){
        if (step_index < tower_move_states.length-1){
            step_index++;
            towers = tower_move_states[step_index];
            display_towers();
        }
        else if (step_index > tower_move_states.length + 10){
            step_index = 0;
            display_towers();
        }
        else{
            step_index++;
            towers = tower_move_states[0];
            display_towers();
        }
    }
}

function clone_object(old_object){
    var new_object = JSON.parse(JSON.stringify(old_object));
    return (new_object);
}

function move1(src, dst){
    rings = towers[src];
    if (rings.length > 0){
        ring = rings.pop();
        towers[dst].push(ring);
    }
    tower_move_states.push(clone_object(towers));
}

function hanoi(n, src, use, dst){
    if(n <= 1){
        move1(src, dst);
    }
    else {
        hanoi(n-1, src, dst, use);
        move1(src, dst);
        hanoi(n-1, use, src, dst);
    }
}

function display_towers() {
    var towers_count = tower_names.length;
    var elem = document.getElementById("towers_canvas");
    var width = elem.width;
    var height = elem.height;
    var tower_margin = width / 20;
    var tower_width = width / 3 - 2 * tower_margin;
    var ring_height = 20;
    var ring_width_pixel = tower_width / 2 / (n+1);
    var ctx = elem.getContext("2d");
    elem.height = height    // clear canvas
    for (i = 0; i < towers_count; i++) {
        var tower_name = tower_names[i];
        var start_x = i * width / 3 + tower_margin;
        var end_x = start_x + tower_width;
        var tower_center = (end_x + start_x) / 2;
        var start_y = height;

        // draw towers
        ctx.fillStyle = "#000000";
        ctx.font = "30px Arial";
        ctx.fillText(tower_name, tower_center-30, 30);

        ctx.fillStyle = "#FF0000";
        ctx.fillRect(start_x, start_y-ring_height, tower_width, ring_height);
        ctx.fillRect(tower_center-5, 100, 10, height - 100 - ring_height);
        start_y -= ring_height;

        // draw rings
        tower_rings = towers[tower_name];
        for (j=0; j < tower_rings.length;j++){
            var ring_width = tower_rings[j];
            var ring_eff_width = ring_width * ring_width_pixel;
            ctx.fillStyle = "#0000FF";
            ctx.fillRect(tower_center-ring_eff_width, start_y-ring_height, ring_eff_width*2, ring_height);
            ctx.fillStyle = "#000000";
            ctx.rect(tower_center-ring_eff_width, start_y-ring_height, ring_eff_width*2, ring_height);
            ctx.stroke();
            start_y -= ring_height;
        }
    }
}

