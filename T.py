import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Create random binary signals for demonstration
np.random.seed(0)
signals = np.random.randint(0, 2, size=(100, 10))

# Define the number of rows and columns for subplots
num_rows = 5  # Number of rows of subplots
num_cols = 2  # Number of columns of subplots

# Create a list to store subplot figures
subplot_figs = []

# Iterate over the signals and create subplots
for i in range(signals.shape[1]):
    # Create a new subplot figure
    fig = go.Figure()

    # Add a scatter trace for the current signal
    fig.add_trace(
        go.Scatter(
            x=np.arange(signals.shape[0]),
            y=signals[:, i],
            mode='markers',
            name=f'Signal {i+1}'
        )
    )

    # Set the subplot layout
    fig.update_layout(
        title=f'Signal {i+1}',
        xaxis=dict(title='Time'),
        yaxis=dict(title='Value'),
        showlegend=True
    )

    # Append the subplot figure to the list
    subplot_figs.append(fig)

# Create the merged plot
fig = make_subplots(rows=num_rows, cols=num_cols, subplot_titles=[f'Signal {i+1}' for i in range(signals.shape[1])])

# Assign each subplot figure to the corresponding subplot position and remove spacing
for i in range(num_rows):
    for j in range(num_cols):
        fig.add_trace(subplot_figs[i * num_cols + j].data[0], row=i+1, col=j+1)
        fig.update_layout(
            {'xaxis' + str(i * num_cols + j + 1): {'anchor': 'y' + str(i * num_cols + j + 1)}},
            {'yaxis' + str(i * num_cols + j + 1): {'anchor': 'x' + str(i * num_cols + j + 1)}}
        )

# Update the merged plot layout
fig.update_layout(height=600, width=800, title_text='Binary Signal Plots', showlegend=False)

# Display the merged plot
fig.show()
