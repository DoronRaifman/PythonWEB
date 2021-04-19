// App.js
document.addEventListener('DOMContentLoaded', function()
{
    console.log('DOM fully loaded and parsed');
    create_graph();
    var myVar = setInterval(my_input_Timer, 100);
});

function my_input_Timer(){
    get_graph_data();
    draw_graph();
}

var trace = {
  y: [10, 20, 30, 40, 50],
  mode: 'lines',
  name: 'Signal data',
   line: {
   color: 'rgb(128, 0, 128)',
   width: 1
  }
};
var graph_data = [trace];

function got_data(result){
    var data = result['graph_data'];
    trace['y'] = data;
}

function get_graph_data() {
    my_ajax_get({}, 'GET', '/get_data', got_data);
}

function create_graph(){
    var layout = {
      title: 'Graph data',
      margin: {autoexpand: false, l: 35, r: 100, t: 30, b: 40, },
      xaxis: {title: 'Time', showgrid: true, },
      yaxis: {title: 'Value', showgrid: true, },
      autotick: true,
      sautosize: true,
      autorange: true,
    };
    Plotly.newPlot('graph', graph_data, layout);
    draw_graph();
}

function draw_graph(){
    Plotly.redraw('graph');
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


