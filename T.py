import numpy as np

# Assuming you have two arrays: temperature_signal and date_time_signal
# temperature_signal: ndarray containing the signal temperatures
# date_time_signal: ndarray containing the corresponding date/time values

# Calculate the time differences in minutes
time_diff = (date_time_signal - date_time_signal[0]).astype('timedelta64[m]')

# Find the indices where the temperature is stable for 30 minutes
stable_indices = np.where(np.diff(temperature_signal) == 0)[0]
stable_indices = stable_indices[np.flatnonzero(np.diff(stable_indices) > 6)]

# Check if the time differences are greater than or equal to 30 minutes for each stable index
stable_indices = stable_indices[np.where(np.diff(time_diff[stable_indices]) >= 30)[0]]

# The filtered indices correspond to the moments where the temperature is stable for 30 minutes
print(stable_indices)


import numpy as np

# Assuming you have two arrays: temperature_signal and date_time_signal
# temperature_signal: ndarray containing the signal temperatures
# date_time_signal: ndarray containing the corresponding date/time values

# Calculate the differences between consecutive temperatures
diff_temperatures = np.diff(temperature_signal)

# Find the indices where the temperature is stable for at least 30 minutes
stable_indices = np.where(diff_temperatures == 0)[0]

# Find the indices where the differences between indices are greater than 1
diff_indices = np.diff(stable_indices)
segment_starts = stable_indices[:-1][np.concatenate(([False], diff_indices > 1))]
segment_ends = stable_indices[:-1][np.concatenate(([diff_indices > 1], [False]))]

# Filter the segments to ensure at least 6 consecutive points
segment_lengths = segment_ends - segment_starts + 1
filtered_starts = segment_starts[segment_lengths >= 6]
filtered_ends = segment_ends[segment_lengths >= 6]

# Find the time differences for each segment
time_diff_starts = date_time_signal[filtered_starts] - date_time_signal[0]
time_diff_ends = date_time_signal[filtered_ends] - date_time_signal[0]

# Find the indices where the segment duration is at least 30 minutes
filtered_start_indices = filtered_starts[time_diff_ends - time_diff_starts >= np.timedelta64(30, 'm')]
filtered_end_indices = filtered_ends[time_diff_ends - time_diff_starts >= np.timedelta64(30, 'm')]

# Print the start and end indices of the stable segments
for start, end in zip(filtered_start_indices, filtered_end_indices):
    print("Start Index:", start)
    print("End Index:", end)
    print("-----")
  
