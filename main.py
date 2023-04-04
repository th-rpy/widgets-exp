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




SQL function to delete fimport.


LearnMeFree
Assume that I have file table (file_id, file_type_id and fimport_id) and file_import with fimport_id. I would a SQL function f_file_import_delete(fimport) that remove a fimport_file with fimport_id. Check if exist a file import with fimport_id (using select count) before delete it and return bool as result 

4 / 4


Here is an example of a SQL function f_file_import_delete that will delete a record from the file_import table with the given fimport_id:

sql
Copy code
CREATE FUNCTION f_file_import_delete(fimport INT) RETURNS BOOLEAN
BEGIN
  DECLARE count_imports INT;
  SELECT COUNT(*) INTO count_imports FROM file_import WHERE fimport_id = fimport;

  IF count_imports = 0 THEN
    RETURN FALSE;
  ELSE
    DELETE FROM file_table WHERE fimport_id = fimport;
    DELETE FROM file_import WHERE fimport_id = fimport;
    RETURN TRUE;
  END IF;
END;
Here's how it works:

The function takes one parameter, fimport, which is the fimport_id of the file import to be deleted.
The DECLARE statement defines a variable count_imports to hold the number of file imports with the given fimport_id.
The SELECT COUNT(*) statement counts the number of file imports with the given fimport_id and stores the result in the count_imports variable.
The IF count_imports = 0 statement checks if there are any file imports with the given fimport_id. If there are none, the function returns FALSE.
If there are file imports with the given fimport_id, the function deletes all records with that fimport_id from both the file_table and file_import tables, and returns TRUE.



LearnMeFree
Datetime as parameter in SQL requete function 

Yes, you can use DATETIME as a parameter in a SQL function. Here's an example of a function that takes a DATETIME parameter and returns the number of records in a table that have a timestamp greater than or equal to the input parameter:

sql
Copy code
CREATE FUNCTION get_recent_records(date_param DATETIME) RETURNS INT
BEGIN
  DECLARE count INT;
  SELECT COUNT(*) INTO count FROM my_table WHERE timestamp >= date_param;
  RETURN count;
END;
In this example, the get_recent_records function takes a DATETIME parameter named date_param. It declares an integer variable count, which is used to store the result of the query that counts the number of records in my_table where the timestamp column is greater than or equal to date_param. Finally, the function returns the count variable.

Note that the syntax for declaring and using parameters in SQL functions may vary depending on the specific database management system you're using.




LearnMeFree
Assume that I have a : 
F_import table: f_import_id, start_date, end_date.
File_type_def : file_type_id, file_type_name,file_type_desc
File: file_id, file_type_id, file_name, file_size, fimport_id
Equipment_files: equip_id, equip_sect_id, file_id 
Equipment_sections: equip_id, equip_sect_id
Equipment_section: equip_sect_id, equip_sect_name
Equipment: equip_id, equip_name.

I would create a function f_file_import_list_get that takes a date_from and date_to as parameters and return all imported files between those two dates. Return file_type_name, file_name, file_size, equip_name, equip_sect_name.
I need a SQL function. First Check if already exists dates from f_import_file table between those dates. 

3 / 3


Here's an example of a SQL function f_file_import_list_get that takes date_from and date_to as parameters and returns the details of all imported files between those two dates. The function also checks if there are any imported files between those dates before returning the results:

sql
Copy code
CREATE FUNCTION f_file_import_list_get(date_from DATETIME, date_to DATETIME) RETURNS TABLE (
  file_type_name VARCHAR(255),
  file_name VARCHAR(255),
  file_size INT,
  equip_name VARCHAR(255),
  equip_sect_name VARCHAR(255)
) 
BEGIN
  DECLARE count_imports INT;
  SELECT COUNT(*) INTO count_imports FROM f_import WHERE start_date >= date_from AND end_date <= date_to;

  IF count_imports = 0 THEN
    RETURN NULL;
  ELSE
    RETURN SELECT ftd.file_type_name, f.file_name, f.file_size, e.equip_name, es.equip_sect_name
      FROM f_import fi
      JOIN file f ON fi.f_import_id = f.f_import_id
      JOIN file_type_def ftd ON f.file_type_id = ftd.file_type_id
      JOIN equipment_files ef ON f.file_id = ef.file_id
      JOIN equipment_sections es ON ef.equip_sect_id = es.equip_sect_id
      JOIN equipment e ON es.equip_id = e.equip_id
      WHERE fi.start_date >= date_from AND fi.end_date <= date_to;
  END IF;
END;
