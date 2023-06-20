# widgets-exp

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
