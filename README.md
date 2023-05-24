
import numpy as np
import datetime as dt

def define_end_date_with_invalid_data(batch_bundle_sigs, kiln_end_pos, kiln_start_pos, locations_sig, times):
    # Find the maximum position in locations_sig
    max_pos = np.nanmax(locations_sig)
    
    if max_pos < kiln_end_pos:
        # If the max position is less than kiln_end_pos
        # Get the last date_time value for the max position
        end_date = batch_bundle_sigs[locations_sig == max_pos]['date_time'][-1].astype(dt.datetime)
    else:
        # Find the indices where location is between kiln_start_pos and max_pos
        mask = np.where((locations_sig < max_pos) & (locations_sig > kiln_start_pos))[0]
        
        # Find the first index where locations_sig is greater than kiln_end_pos
        first_index = np.argmax(locations_sig[mask] > kiln_end_pos)
        
        if locations_sig[mask][first_index] - kiln_end_pos < 10:
            # If the difference between locations_sig and kiln_end_pos is less than 10
            # Set the end_date to the corresponding time value
            end_date = times[mask][first_index].astype(dt.datetime)
        else:
            # Find the indices where location is less than kiln_end_pos
            indices = np.where(locations_sig < kiln_end_pos)[0]
            
            # Find the first index where locations_sig is maximum
            first_index = np.argmax(locations_sig[indices])
            
            # Set the end_date to the corresponding time value
            end_date = times[indices][first_index].astype(dt.datetime)
    
    return end_date


import unittest
import numpy as np
import datetime as dt

class TestDefineEndDate(unittest.TestCase):
    def test_valid_end_date(self):
        batch_bundle_sigs = np.array([
            {'locations_sig': 5, 'date_time': np.array(['2023-05-23 10:00:00', '2023-05-23 11:00:00'], dtype='datetime64')}
        ])
        kiln_end_pos = 10
        kiln_start_pos = 3
        locations_sig = np.array([2, 4, 6, 8, 10, 12, 14])
        times = np.array(['2023-05-23 09:00:00', '2023-05-23 10:00:00', '2023-05-23 11:00:00',
                          '2023-05-23 12:00:00', '2023-05-23 13:00:00', '2023-05-23 14:00:00',
                          '2023-05-23 15:00:00'], dtype='datetime64')
        
        expected_end_date = dt.datetime(2023, 5, 23, 11, 0, 0)
        end_date = define_end_date_with_invalid_data(batch_bundle_sigs, kiln_end_pos, kiln_start_pos, locations_sig, times)
        self.assertEqual(end_date, expected_end_date)

    def test_invalid_end_date(self):
        batch_bundle_sigs = np.array([
            {'locations_sig': 15, 'date_time': np.array(['2023-05-23 10:00:00', '2023-05-23 11:00:00'], dtype='datetime64')}
        ])
        kiln_end_pos = 10
        kiln_start_pos = 3
        locations_sig = np.array([2, 4, 6, 8, 10, 12, 14])
        times = np.array(['2023-05-23 09:00:00', '2023-05-23 10:00:00', '2023-05-23 11:00:00',
                          '2023-05-23 12:00:00', '2023-05-23 13:00:00', '2023-05-23 14:00:00',
                          '2023-05-23 15:00:00'], dtype='datetime64')
        
        expected_end_date = dt.datetime(2023, 5, 23, 14, 0, 0)
        end_date = define_end_date_with_invalid_data(batch_bundle_sigs, kiln_end_pos, kiln_start_pos, locations_sig, times)
        self.assertEqual(end_date, expected_end_date)

if __name__ == '__main__':
    unittest.main()


