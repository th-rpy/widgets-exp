# Create a list to store scatter traces for each signal
traces = []

# Iterate over the signals and create scatter traces
for i in range(signals.shape[1]):
    trace = go.Scatter(
        x=np.arange(signals.shape[0]),
        y=signals[:, i],
        mode='markers',
        name=f'Signal {i+1}'
    )
    traces.append(trace)

# Create the layout
layout = go.Layout(
    title='Binary Signal Plots',
    xaxis=dict(title='Time'),
    yaxis=dict(title='Value'),
    showlegend=True
)

# Create the figure with all scatter traces
fig = go.Figure(data=traces, layout=layout)

# Set the spacing between subplots to zero
fig.update_layout(
    margin=dict(t=40, r=40, b=40, l=40),
    xaxis=dict(domain=[0, 1], anchor='y'),
    yaxis=dict(domain=[0, 1], anchor='x'),
    xaxis2=dict(domain=[0, 1], anchor='y2'),
    yaxis2=dict(domain=[0, 1], anchor='x2'),
    xaxis3=dict(domain=[0, 1], anchor='y3'),
    yaxis3=dict(domain=[0, 1], anchor='x3'),
    xaxis4=dict(domain=[0, 1], anchor='y4'),
    yaxis4=dict(domain=[0, 1], anchor='x4'),
    xaxis5=dict(domain=[0, 1], anchor='y5'),
    yaxis5=dict(domain=[0, 1], anchor='x5'),
    xaxis6=dict(domain=[0, 1], anchor='y6'),
    yaxis6=dict(domain=[0, 1], anchor='x6'),
    xaxis7=dict(domain=[0, 1], anchor='y7'),
    yaxis7=dict(domain=[0, 1], anchor='x7'),
    xaxis8=dict(domain=[0, 1], anchor='y8'),
    yaxis8=dict(domain=[0, 1], anchor='x8'),
    xaxis9=dict(domain=[0, 1], anchor='y9'),
    yaxis9=dict(domain=[0, 1], anchor='x9'),
    xaxis10=dict(domain=[0, 1], anchor='y10'),
    yaxis10=dict(domain=[0, 1], anchor='x10')
)

# Display the figure
fig.show()
