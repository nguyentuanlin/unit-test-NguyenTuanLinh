import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO

# Thêm src vào sys.path để import module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from module import count_excellent_students, calculate_valid_average, main

class TestScoreFunctions(unittest.TestCase):
    def test_excellent_all_valid(self):
        self.assertEqual(count_excellent_students([8.0, 9.5, 10.0]), 3)

    def test_excellent_mixed_valid_invalid(self):
        self.assertEqual(count_excellent_students([8.0, 7.5, -1, 11, 9.0]), 2)

    def test_excellent_all_below_8(self):
        self.assertEqual(count_excellent_students([6.0, 7.9, 5.0]), 0)

    def test_excellent_empty_list(self):
        self.assertEqual(count_excellent_students([]), 0)

    def test_excellent_none_input(self):
        self.assertEqual(count_excellent_students(None), 0)

    def test_excellent_with_none_values_inside(self):
        self.assertEqual(count_excellent_students([8.5, None, 9.0]), 2)

    def test_excellent_with_all_invalid_scores(self):
        self.assertEqual(count_excellent_students([-5, 12, None]), 0)

    def test_average_all_valid(self):
        self.assertAlmostEqual(calculate_valid_average([7.0, 8.0, 9.0]), 8.0)

    def test_average_mixed_valid_invalid(self):
        self.assertAlmostEqual(calculate_valid_average([7.0, -2, 10.0, 12]), 8.5)

    def test_average_empty_list(self):
        self.assertEqual(calculate_valid_average([]), 0.0)

    def test_average_none_input(self):
        self.assertEqual(calculate_valid_average(None), 0.0)

    def test_average_no_valid_scores(self):
        self.assertEqual(calculate_valid_average([-1, 11, None]), 0.0)

    def test_average_single_valid_score(self):
        self.assertEqual(calculate_valid_average([9.0]), 9.0)

    def test_average_with_none_values_inside(self):
        self.assertAlmostEqual(calculate_valid_average([9.0, None, 6.0]), 7.5)

class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', return_value='9.5,8,7,-1,11')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_valid_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Số học sinh đạt loại Giỏi (>=8.0): 2", output)
        self.assertIn("Điểm trung bình hợp lệ (0-10): 8.17", output)

    @patch('builtins.input', return_value='abc, 8, 9')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_invalid_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Lỗi: Vui lòng chỉ nhập số thực cách nhau bởi dấu phẩy.", output)

if __name__ == "__main__":
    unittest.main()  # pragma: no cover
