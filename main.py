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
