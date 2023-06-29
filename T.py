import plotly.graph_objects as go
import numpy as np

# Create random binary signals for demonstration
np.random.seed(0)
signals = np.random.randint(0, 2, size=(100, 10))

# Define the number of rows and columns for the grid
num_rows = 5  # Number of rows in the grid
num_cols = 2  # Number of columns in the grid

# Create a figure with subplots
fig = make_subplots(rows=num_rows, cols=num_cols, subplot_titles=[f'Signal {i+1}' for i in range(signals.shape[1])])

# Iterate over the signals and add binary plots to the subplots
for i in range(signals.shape[1]):
    # Calculate the row and column index of the current subplot
    row = (i // num_cols) + 1
    col = (i % num_cols) + 1

    # Create a scatter trace for the binary signal
    scatter_trace = go.Scatter(
        x=np.arange(signals.shape[0]),
        y=signals[:, i],
        mode='markers',
        name=f'Signal {i+1}'
    )



import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(
            id='graph1',
            figure={
                'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Graph 1'}],
                'layout': {'title': 'Graph 1'}
            },
            style={'height': '50%'}
        ),
        html.Hr(),
        dcc.Graph(
            id='graph2',
            figure={
                'data': [{'x': [1, 2, 3], 'y': [2, 4, 1], 'type': 'bar', 'name': 'Graph 2'}],
                'layout': {'title': 'Graph 2'}
            },
            style={'height': '50%'}
        ),
        html.Div(
            id='horizontal-line',
            style={
                'width': '100%',
                'height': '2px',
                'background-color': 'black',
                'position': 'relative',
                'top': '50%',
                'transform': 'translateY(-50%)'
            },
            draggable=True
        ),
        dcc.Input(id='drag-value', type='hidden')
    ],
    id='main-container'
)

app.scripts.append_script(
    """
    document.addEventListener('DOMContentLoaded', function() {
        var dragValue = 0;
        var dragStartY = 0;
        var line = document.getElementById('horizontal-line');
        var input = document.getElementById('drag-value');
        var container = document.getElementById('main-container');

        line.addEventListener('dragstart', function(e) {
            dragStartY = e.clientY;
        });

        container.addEventListener('dragover', function(e) {
            e.preventDefault();
        });

        container.addEventListener('dragenter', function(e) {
            e.preventDefault();
        });

        container.addEventListener('drop', function(e) {
            var dragEndY = e.clientY;
            dragValue = dragEndY - dragStartY;
            input.value = dragValue;
            input.dispatchEvent(new Event('change'));
        });
    });
    """
)

@app.callback(
    Output('graph1', 'style'),
    Output('graph2', 'style'),
    Input('drag-value', 'value'),
    State('graph1', 'style'),
    State('graph2', 'style')
)
def update_graph_height(drag_value, graph1_style, graph2_style):
    if drag_value is None:
        return graph1_style, graph2_style

    drag_value = int(drag_value)
    graph1_height = int(graph1_style['height'].strip('%'))
    graph2_height = int(graph2_style['height'].strip('%'))
    max_height = 100

    if drag_value < 0 and graph1_height > 0:
        graph1_height -= abs(drag_value)
        graph2_height += abs(drag_value)
    elif drag_value > 0 and graph2_height > 0:
        graph1_height += abs(drag_value)
        graph2_height -= abs(drag_value)

    graph1_style['height'] = f'{graph1_height}%'
    graph2_style['height'] = f'{graph2_height}%'

    return graph1_style, graph2_style

if __name__ == '__main__':
    app.run_server(debug=True)


    # Add the scatter trace to the subplot
    fig.add_trace(scatter_trace, row=row, col=col)

    # Update the layout of the subplot
    fig.update_xaxes(title='Time', row=row, col=col)
    fig.update_yaxes(title='', tickvals=[0, 1], ticktext=['0', '1'], row=row, col=col)

# Update the layout of the grid
fig.update_layout(height=600, width=800, title_text='Binary Signal Grid')

# Display the grid graph
fig.show()


// dragHandler function
function dragHandler(dragValue, existingData) {
  const newDragValue = parseFloat(dragValue);
  const newData = Object.assign({}, existingData);
  newData.dragValue = newDragValue;
  return newData;
}

// updateGraphHeight function
function updateGraphHeight(data, graph1Style, graph2Style) {
  if (!data || !data.dragValue) {
    return [graph1Style, graph2Style];
  }

  const dragValue = parseInt(data.dragValue);
  const graph1Height = parseInt(graph1Style.height.replace('%', ''));
  const graph2Height = parseInt(graph2Style.height.replace('%', ''));
  const maxHeight = 100;

  if (dragValue < 0 && graph1Height > 0) {
    graph1Style.height = `${graph1Height - Math.abs(dragValue)}%`;
    graph2Style.height = `${graph2Height + Math.abs(dragValue)}%`;
  } else if (dragValue > 0 && graph2Height > 0) {
    graph1Style.height = `${graph1Height + Math.abs(dragValue)}%`;
    graph2Style.height = `${graph2Height - Math.abs(dragValue)}%`;
  }

  return [graph1Style, graph2Style];
}


      app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='dragHandler'
    ),
    Output('drag-store', 'data'),
    [Input('drag-value', 'value')],
    [State('drag-store', 'data')]
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='updateGraphHeight'
    ),
    [Output('graph1', 'style'), Output('graph2', 'style')],
    [Input('drag-store', 'data')],
    [State('graph1', 'style'), State('graph2', 'style')]
)



,
        html.Script(
            """
            document.addEventListener("DOMContentLoaded", function() {
                var line = document.getElementById("horizontal-line");
                var graph1 = document.getElementById("graph1");
                var graph2 = document.getElementById("graph2");
                var initialY = 0;
                var initialHeight = 0;

                line.addEventListener("mousedown", function(e) {
                    initialY = e.clientY;
                    initialHeight = parseFloat(graph1.style.height);
                    document.addEventListener("mousemove", resizeGraphs);
                    document.addEventListener("mouseup", removeEventListeners);
                });

                function resizeGraphs(e) {
                    var deltaY = e.clientY - initialY;
                    var newHeight = initialHeight + (deltaY / window.innerHeight) * 100;
                    var graph1Height = Math.max(Math.min(newHeight, 100), 0) + "%";
                    var graph2Height = Math.max(100 - newHeight, 0) + "%";

                    graph1.style.height = graph1Height;
                    graph2.style.height = graph2Height;
                }

                function removeEventListeners() {
                    document.removeEventListener("mousemove", resizeGraphs);
                    document.removeEventListener("mouseup", removeEventListeners);
                }
            });
            """
        ),
