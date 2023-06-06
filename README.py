# widgets-exp

import unittest
from typing import List
from your_module import YourClass, PlotGroupInfo

class YourClassTests(unittest.TestCase):
    def setUp(self):
        # Initialize your class instance
        self.obj = YourClass()

    def test_get_plot_group_list_with_valid_id(self):
        # Arrange
        file_type_id = 1

        # Act
        result = self.obj.get_plot_group_list(file_type_id)

        # Assert
        self.assertIsInstance(result, List[PlotGroupInfo])
        self.assertGreater(len(result), 0)

    def test_get_plot_group_list_with_invalid_id(self):
        # Arrange
        file_type_id = -1

        # Act
        result = self.obj.get_plot_group_list(file_type_id)

        # Assert
        self.assertIsInstance(result, List[PlotGroupInfo])
        self.assertEqual(len(result), 0)

    def test_get_plot_group_list_with_none_result(self):
        # Arrange
        file_type_id = 2  # Assuming this ID returns None

        # Act
        result = self.obj.get_plot_group_list(file_type_id)

        # Assert
        self.assertIsInstance(result, List[PlotGroupInfo])
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()
