import unittest
import data_viz as dv
import random

class TestMathLib(unittest.TestCase):

    def test_boxplot_file_type(self):
        L = [8, 4, 1, 2, 6, 2]
        x_ticks = "sample1"
        with self.assertRaises(ValueError) as ex:
            dv.boxplot('test.jpeg', 'title', 'x_axis', 'y_axis', L, x_ticks)
        message = 'File type not supported'
        self.assertEqual(str(ex.exception), message)

    def test_histogram_file_type(self):
        L = [8, 4, 1, 2, 6, 2]
        with self.assertRaises(ValueError) as ex:
            dv.histogram(L, 'test.jpeg')
        message = 'File type not supported'
        self.assertEqual(str(ex.exception), message)

    def test_combo_file_type(self):
        L = [8, 4, 1, 2, 6, 2]
        with self.assertRaises(ValueError) as ex:
            dv.combo(L, 'test.jpeg')
        message = 'File type not supported'
        self.assertEqual(str(ex.exception), message)

if __name__ == '__main__':
    unittest.main()
