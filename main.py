import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display

# Load the data and create a list of KPIs
data = pd.read_csv('my_data.csv')
kpi_list = data.columns.tolist()

# Define the title and description
title = widgets.HTML("<h1>KPI Analysis</h1>")
description = widgets.HTML("<p>This widget allows you to analyze your key performance indicators.</p>")
display(title)
display(description)

# Define the dropdowns and checkbox
kpi1_dropdown = widgets.Dropdown(options=kpi_list, description='KPI 1:')
kpi2_dropdown = widgets.Dropdown(options=kpi_list, description='KPI 2:', disabled=True)
checkbox = widgets.Checkbox(description='Enable KPI 2')

# Define the update function for the checkbox
def update_checkbox(change):
    if change['new']:
        kpi2_dropdown.disabled = False
    else:
        kpi2_dropdown.disabled = True

checkbox.observe(update_checkbox, 'value')

# Define the plot type dropdown and button
plot_type_dropdown = widgets.Dropdown(options=['line', 'scatter', 'box', 'histogram', 'bar'], description='Plot Type:')
plot_button = widgets.Button(description='Generate Plot')

# Define the update function for the plot button
def update_plot(button):
    kpi1 = kpi1_dropdown.value
    kpi2 = kpi2_dropdown.value
    plot_type = plot_type_dropdown.value
    fig = None
    
    if kpi2:
        fig = px.scatter(data, x=kpi2, y=kpi1, color=data['date_time'], trendline='ols')
    else:
        if plot_type == 'line':
            fig = px.line(data, x='date_time', y=kpi1)
        elif plot_type == 'scatter':
            fig = px.scatter(data, x='date_time', y=kpi1, color=data['date_time'])
        elif plot_type == 'box':
            fig = px.box(data, x='date_time', y=kpi1)
        elif plot_type == 'histogram':
            fig = px.histogram(data, x=kpi1)
        elif plot_type == 'bar':
            fig = px.bar(data, x='date_time', y=kpi1)
    
    fig.show()

plot_button.on_click(update_plot)

# Display the widgets
display(kpi1_dropdown)
display(checkbox)
display(kpi2_dropdown)
display(plot_type_dropdown)
display(plot_button)



# 
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from ipywidgets import interact, Dropdown, Checkbox, Button, Output, HBox, VBox
from scipy import stats

# Load sample data
data = pd.read_csv('sample_data.csv')
data['date_time'] = pd.to_datetime(data['date_time'])

# Create KPI Analysis dashboard widgets
title = "<h1>KPI Analysis</h1>"
description = "<p>Select one or two KPIs to analyze, choose a plot type, and click the button to generate the plot.</p>"
title_widget = Output()
description_widget = Output()
with title_widget:
    display(title)
with description_widget:
    display(description)

kpi1_dropdown = Dropdown(options=data.columns, value=data.columns[0], description='KPI 1:')
kpi2_dropdown = Dropdown(options=data.columns, value=data.columns[1], description='KPI 2:', disabled=True)
def checkbox_change(change):
    kpi2_dropdown.disabled = not change['new']
checkbox = Checkbox(description='Compare two KPIs', value=False)
checkbox.observe(checkbox_change, 'value')

plot_types = ['line', 'scatter', 'box', 'histogram', 'bar']
plot_dropdown = Dropdown(options=plot_types, value=plot_types[0], description='Plot Type:')
plot_button = Button(description='Generate Plot')
plot_output = Output()
description_output = Output()

# Define function to generate plot based on selected options
def generate_plot(kpi1, kpi2, plot_type):
    fig = px.scatter(data, x='date_time', y=kpi1, trendline='ols')
    if kpi2 is not None:
        fig.add_scatter(x=data[kpi2], y=data[kpi1], mode='markers', marker=dict(color='red'), name='Outliers')
    if plot_type == 'line':
        fig.update_traces(mode='lines+markers')
    elif plot_type == 'box':
        fig = px.box(data, x='date_time', y=kpi1)
    elif plot_type == 'histogram':
        fig = px.histogram(data, x=kpi1)
    elif plot_type == 'bar':
        fig = px.bar(data, x='date_time', y=kpi1)
    elif plot_type == 'scatter':
        # Detect outliers using z-score
        z_scores = np.abs(stats.zscore(data[kpi1]))
        threshold = 3
        outliers = data[z_scores > threshold]
        # Add outlier markers to plot
        fig.add_scatter(x=outliers['date_time'], y=outliers[kpi1], mode='markers', marker=dict(color='red'), name='Outliers')
    plot_output.clear_output()
    with plot_output:
        fig.show()
    description_output.clear_output()
    with description_output:
        desc = f"<p><b>{kpi1}</b> statistics: Max = {data[kpi1].max()}, Min = {data[kpi1].min()}, Mean = {data[kpi1].mean()}, Median = {data[kpi1].median()}</p>"
        display(desc)

# Define function to handle plot button click
def plot_button_click(b):
    kpi1 = kpi1_dropdown.value
    kpi2 = kpi2_dropdown.value if not kpi2_dropdown.disabled else None
    plot_type = plot_dropdown.value
    generate_plot(kpi1, kpi2, plot_type)

plot_button.on_click(plot_button_click)

# Display the KPI Analysis dashboard
display(title_widget)
display(description_widget)
display(HBox([kpi1_dropdown, checkbox, kpi2_dropdown]))
display(plot_dropdown)
display(plot_button)
display(VBox([plot_output, description_output]))










import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display

# Load a sample dataset
data = pd.read_csv('sample_data.csv')

# Create a list of draggable widgets for each column
column_widgets = [widgets.HTML(value=f'<h4>{col}</h4>', draggable=True) for col in data.columns]

# Create a vertical box container for the column widgets
column_container = widgets.VBox(column_widgets)

# Create a plot output widget
plot_output = widgets.Output()

# Define a function to update the plot when the columns and date time axis are changed
def update_plot(change):
    with plot_output:
        plot_output.clear_output()
        fig = px.line(data, x='datetime', y=column_dropdown.value)
        fig.update_layout(title=f'{column_dropdown.value} over Time')
        fig.show()

# Create a dropdown widget for selecting the column to plot
column_dropdown = widgets.Dropdown(
    options=list(data.columns),
    description='Column:',
    disabled=False
)

# Create a horizontal box container for the column dropdown and plot output
control_container = widgets.HBox([column_dropdown, plot_output])

# Link the column dropdown to the update function
column_dropdown.observe(update_plot, names='value')

# Add an event listener to the container to update the columns when they are moved
def update_columns_order(change):
    data.columns = [widget.value.split('<h4>')[1].split('</h4>')[0] for widget in column_container.children]
    update_plot(None)
    
column_container.observe(update_columns_order, names='children')

# Display the containers
display(widgets.VBox([column_container, control_container]))





