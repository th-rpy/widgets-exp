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

    # Add the scatter trace to the subplot
    fig.add_trace(scatter_trace, row=row, col=col)

    # Update the layout of the subplot
    fig.update_xaxes(title='Time', row=row, col=col)
    fig.update_yaxes(title='', tickvals=[0, 1], ticktext=['0', '1'], row=row, col=col)

# Update the layout of the grid
fig.update_layout(height=600, width=800, title_text='Binary Signal Grid')

# Display the grid graph
fig.show()
