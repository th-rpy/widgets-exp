from dataclasses import dataclass
import re
import datetime as dt
import numpy as np

@dataclass 
class FileData:
    start_date: dt.datetime 
    end_date: dt.datetime 
    target_mc: float
    final_mc: float 
    values: np.ndarray 
    

def _convert_to_dt_object(date_string: str)->dt.datetime:
    # Remove extra spaces from the date string
    date_string = " ".join(date_string.split())

    # Define the format of the date string
    date_format = "%a %I:%M:%S%p %b %d %y"

    # Parse the date string and return the datetime object
    dt_obj = dt.datetime.strptime(date_string, date_format)
    return dt_obj


def _manipulate_datetime(datetime_string: str)->dt.datetime:
    datetime_string = datetime_string.strip()
    date_str, time_str = datetime_string.split(' ')

    year, month, day = map(int, date_str.split('-'))
    hours, minutes, seconds = map(int, time_str.split(':'))

    additional_days, hours = divmod(hours, 24)

    manipulated_datetime = dt.datetime(year, month, day, hours, minutes, seconds) + dt.timedelta(days=additional_days)

    return manipulated_datetime

def _get_value_from_line(content, pattern):
    lines_matching_pattern = [line for line in content if pattern in line]
    value_matched = next(
        (re.search(f"{pattern}:(.*)", line) for line in lines_matching_pattern),
        None,
    )
    if value_matched:
        return value_matched.group(1).strip()
    raise ValueError("Pattern not found in the content")


def _get_idx_and_columns_of_data_table(content, pattern):
    lines_matching_pattern = [(idx, line) for idx, line in enumerate(content) if line.startswith(pattern)]
    if len(lines_matching_pattern) >= 2:
        idx, runtime_data = lines_matching_pattern[1]
        value_matched = re.search(pattern + r'\s+(.+)', runtime_data)
        if value_matched:
            return idx, ['Runtime'] + value_matched.group(1).strip().split('\t')
    raise ValueError("Pattern not found in the content or does not have a second index")

def _transform_to_array(content, start_index, columns, start_date):
    # Columns and types
    columns_types = [('date_time', 'datetime64[s]')] + [(field, '<f4') for field in columns[1:]]
    
    # Data
    lines = content[start_index + 1:]
    data = [line.strip().split('\t') for line in lines]

    # Initialize array with column types
    data_values = np.zeros(len(data), dtype=columns_types)
    
    # Fill array with values
    trig_date = str(start_date).split(' ')[0]
    data_values['date_time'] = np.array([_manipulate_datetime(f'{trig_date} {values[0]}') for values in data])
    for field in columns[1:]:
        data_values[field] = np.array(list(map(float, [values[columns.index(field)] for values in data])))
    
    return data_values

def _read_file(path):
    # Read the content from the text file
    with open(path, "r") as file:
        content = file.readlines()
    return content

def extract_file_data(path):
    
    content = _read_file(path="06230628.txt")
    # Extract start date
    start_date = _get_value_from_line(content, "Start")
    start_date = _convert_to_dt_object(start_date)

    # Extract end date
    end_date = _get_value_from_line(content, "Stop")
    end_date = _convert_to_dt_object(end_date)

    # Extract target MC
    target_mc = _get_value_from_line(content, "Target MC")
    target_mc = float(target_mc)

    # Extract final MC
    final_mc = _get_value_from_line(content, "Final MC")
    final_mc = float(final_mc)

    # Extract values
    idx, columns = _get_idx_and_columns_of_data_table(content, 'Runtime')
    mc_values = _transform_to_array(content, idx, columns, start_date)
    return FileData(start_date, end_date, target_mc, final_mc, mc_values)

print(extract_file_data('06230628.txt').values.dtype.names)







import datetime as dt
import numpy as np
import pytest
from test import _convert_to_dt_object, _get_idx_and_columns_of_data_table, _get_value_from_line, _manipulate_datetime, _transform_to_array, extract_file_data

class TestConvertToDtObj: 
    def test_valid_date_string(self):
        # Test case 1: Valid date string
        date_string = "Mon 08:20:09pm Jun 26 23"
        expected_result = dt.datetime(2023, 6, 26, 20, 20, 9)
        assert _convert_to_dt_object(date_string) == expected_result
    def test_valid_date_string_with_spaces(self):
        # Test case 2: Valid date string with leading/trailing spaces
        date_string = "   Wed 02:42:35am  Jun 28 23   "
        expected_result = dt.datetime(2023, 6, 28, 2, 42, 35)
        assert _convert_to_dt_object(date_string) == expected_result
    def test_with_different_format(self):
        # Test case 3: Valid date string with different format
        date_string = "Fri 12:00:00AM Sep 01 23"
        expected_result = dt.datetime(2023, 9, 1, 0, 0, 0)
        assert _convert_to_dt_object(date_string) == expected_result
    def test_invalid_date_string(self):
        # Test case 4: Invalid date string
        date_string = "Invalid date string"
        with pytest.raises(ValueError):
            _convert_to_dt_object(date_string)

        # Test case 5: Empty date string
        date_string = ""
        with pytest.raises(ValueError):
            _convert_to_dt_object(date_string)
        

class TestManipulateDateTime:
    def test_valid_datetime_string(self):
        datetime_string = '2023-06-26 30:22:10'
        expected_result = dt.datetime(2023, 6, 27, 6, 22, 10)
        assert _manipulate_datetime(datetime_string) == expected_result

    def test_valid_datetime_string_with_spaces(self):
        datetime_string = '  2023-09-15 12:30:45  '
        expected_result = dt.datetime(2023, 9, 15, 12, 30, 45)
        assert _manipulate_datetime(datetime_string) == expected_result

    def test_valid_datetime_string_different_date_time(self):
        datetime_string = '2024-01-01 10:15:30'
        expected_result = dt.datetime(2024, 1, 1, 10, 15, 30)
        assert _manipulate_datetime(datetime_string) == expected_result

    def test_invalid_datetime_string(self):
        datetime_string = 'Invalid datetime string'
        with pytest.raises(ValueError):
            _manipulate_datetime(datetime_string)

    def test_empty_datetime_string(self):
        datetime_string = ''
        with pytest.raises(ValueError):
            _manipulate_datetime(datetime_string)


class TestGetValueFromLine:
    def test_start_pattern(self):
        content = [
            "Start: Mon 08:20:09pm Jun 26 23\n",
            "Stop: Wed 02:42:35am Jun 28 23\n",
            "Target MC: 16.3\n",
            "Runtime: 30:22:10\n",
        ]
        pattern = 'Start'
        expected_result = 'Mon 08:20:09pm Jun 26 23'
        assert _get_value_from_line(content, pattern) == expected_result

    def test_stop_pattern(self):
        content = [
            "Start: Mon 08:20:09pm Jun 26 23\n",
            "Stop: Wed 02:42:35am Jun 28 23\n",
            "Target MC: 16.3\n",
            "Runtime: 30:22:10\n",
        ]
        pattern = 'Stop'
        expected_result = 'Wed 02:42:35am Jun 28 23'
        assert _get_value_from_line(content, pattern) == expected_result

    def test_target_mc_pattern(self):
        content = [
            "Start: Mon 08:20:09pm Jun 26 23\n",
            "Stop: Wed 02:42:35am Jun 28 23\n",
            "Target MC: 16.3\n",
            "Runtime: 30:22:10\n",
        ]
        pattern = 'Target MC'
        expected_result = '16.3'
        assert _get_value_from_line(content, pattern) == expected_result

    def test_runtime_pattern(self):
        content = [
            "Start: Mon 08:20:09pm Jun 26 23\n",
            "Stop: Wed 02:42:35am Jun 28 23\n",
            "Target MC: 16.3\n",
            "Runtime: 30:22:10\n",
        ]
        pattern = 'Runtime'
        expected_result = '30:22:10'
        assert _get_value_from_line(content, pattern) == expected_result

    def test_pattern_not_found(self):
        content = [
            "Start: Mon 08:20:09pm Jun 26 23\n",
            "Stop: Wed 02:42:35am Jun 28 23\n",
            "Target MC: 16.3\n",
            "Runtime: 30:22:10\n",
        ]
        pattern = 'InvalidPattern'
        with pytest.raises(ValueError):
            _get_value_from_line(content, pattern)



class TestTransformToArray:
    def setup_data(self):
        content = [
            "Runtime\tMC 1\tMC 2\tMC 3\n",
            "20:27:30\t28.4\t27.8\t26.1\n",
            "20:28:04\t28.4\t27.8\t26.1\n",
            "20:33:05\t28.3\t27.7\t26.0\n",
            "20:38:05\t28.2\t27.6\t25.9\n",
            "20:43:05\t28.1\t27.4\t25.9\n",
            "20:48:05\t27.9\t27.3\t25.8\n",
            "20:53:05\t27.8\t27.2\t25.7\n",
        ]

        start_index = 0
        columns = ['Runtime', 'MC 1', 'MC 2', 'MC 3']
        start_date = dt.datetime(2023, 6, 26)
        return content, start_index, columns, start_date
    def test_transform_to_array(self):
        content, start_index, columns, start_date = self.setup_data()
        expected_array = np.array([
            ('2023-06-26T20:27:30', 28.4, 27.8, 26.1),
            ('2023-06-26T20:28:04', 28.4, 27.8, 26.1),
            ('2023-06-26T20:33:05', 28.3, 27.7, 26.0),
            ('2023-06-26T20:38:05', 28.2, 27.6, 25.9),
            ('2023-06-26T20:43:05', 28.1, 27.4, 25.9),
            ('2023-06-26T20:48:05', 27.9, 27.3, 25.8),
            ('2023-06-26T20:53:05', 27.8, 27.2, 25.7),
        ],
            dtype=[('date_time', 'datetime64[s]'), ('MC 1', '<f4'), ('MC 2', '<f4'), ('MC 3', '<f4')]
        )

        result_array = _transform_to_array(content, start_index, columns, start_date)
        np.testing.assert_array_equal(result_array, expected_array)

    def test_transform_to_array_empty_content(self):
        _, start_index, columns, start_date = self.setup_data()
        content = []
        expected_array = np.zeros(0, dtype=[('date_time', 'datetime64[s]'), ('MC 1', '<f4'), ('MC 2', '<f4'), ('MC 3', '<f4')])
        result_array = _transform_to_array(content, start_index, columns, start_date)
        np.testing.assert_array_equal(result_array, expected_array)

    def test_transform_to_array_invalid_start_date(self):
        content, start_index, columns, _ = self.setup_data()
        with pytest.raises(ValueError):
            _transform_to_array(content, start_index, columns, 'InvalidStartDate')


class TestGetIdxAndColumnsOfDataTable:
    def setup_data(self):
        content = [
            "Usage: 178431\n",
            "Usage/BdFt: 0.80\n",
            "Comment: \n",
            "Start: Mon 08:20:09pm Jun 26 23\n",
            "Stop: Wed 02:42:35am Jun 28 23\n",
            "Runtime: 30:22:10\n",
            "Elapsed Time: 30:22:26\n",
            "Est Drying Time: 00:00:00\n",
            "Advance Shortened: 09:43:50\n",
            "Shutdown: 0\n",
            "Target MC: 16.3\n",
            "Final MC: 16.0\n",
            "Drying MC: 16.2\n",
            "Species: SPF\n",
            "Use Meas MC: 1\n",
            "\n",
            "Runtime\tEntAir\tExAir\tWetBulb\tEntAirLmt\tExAirSp\tWetBulbSp\tMode\tMeasMC\tMcSetPt\tAction\tMC 1\tMC 2\tMC 3\n",
            "20:27:30    185    195    150    200    195    150    3    26.69    16.3    0    28.4    27.8    26.1\n",
            "20:28:04    185    194    150    200    195    150    3    26.69    16.3    0    28.4    27.8    26.1\n",
            "20:33:05    185    195    150    200    195    149    3    26.57    16.3    0    28.3    27.7    26.0\n",
            "20:38:05    185    195    149    200    195    149    3    26.48    16.3    0    28.2    27.6    25.9\n",
            "20:43:05    185    195    149    200    195    149    3    26.39    16.3    0    28.1    27.4    25.9\n",
            "20:48:05    185    195    149    199    195    148    3    26.29    16.3    0    27.9    27.3    25.8\n",
            "20:53:05    185    194    149    199    195    148    3    26.16    16.3    0    27.8    27.2    25.7\n",
        ]

        pattern = 'Runtime'
        return content, pattern 

    def test_get_idx_and_columns_of_data_table(self):
        content, pattern = self.setup_data()
        expected_idx = 16
        expected_columns = ['Runtime', 'EntAir', 'ExAir', 'WetBulb', 'EntAirLmt', 
                            'ExAirSp', 'WetBulbSp', 'Mode', 'MeasMC', 'McSetPt', 
                            'Action', 'MC 1', 'MC 2', 'MC 3']

        result_idx, result_columns = _get_idx_and_columns_of_data_table(content, pattern)
        print(result_columns)
        assert result_idx == expected_idx
        assert result_columns == expected_columns

    def test_get_idx_and_columns_of_data_table_invalid_pattern(self):
        content, pattern = self.setup_data()
        pattern = 'InvalidPattern'
        with pytest.raises(ValueError):
            _get_idx_and_columns_of_data_table(content, pattern)
            
            
class TestExtractFileData:
    def test_extract_file_data(self):
        path = "06230628.txt"
        expected_start_date = dt.datetime(2023, 6, 26, 20, 20, 9)
        expected_end_date = dt.datetime(2023, 6, 28, 2, 42, 35)
        expected_target_mc = 16.3
        expected_final_mc = 16.0
        expected_dtypes = ('date_time', 'EntAir', 'ExAir', 'WetBulb', 
                                     'EntAirLmt', 'ExAirSp', 'WetBulbSp', 'Mode', 
                                     'MeasMC', 'McSetPt', 'Action', 'MC 1', 'MC 2',
                                     'MC 3', 'MC 4', 'MC 5', 'MC 6', 'MC 7', 'MC 8', 
                                     'TDAL', 'TDalMult', 'TDALMC', 'Demand', 'FanDir', 'FanSpd', 'Amps1 ',
                                     'Amps2 ', 'Mtr1 ', 'Mtr2 ', 'Mtr3 ', 'Mtr4 ', 'Mtr5 ', 
                                     'Mtr6 ', 'Mtr7 ', 'Mtr8 ', 'Mtr9 ', 'Mtr10')
        
        result = extract_file_data(path)
        
        assert result.start_date == expected_start_date
        assert result.end_date == expected_end_date
        assert result.target_mc == expected_target_mc
        assert result.final_mc == expected_final_mc
        assert result.values.dtype.names == expected_dtypes

