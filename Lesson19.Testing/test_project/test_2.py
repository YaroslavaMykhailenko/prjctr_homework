import unittest

from max import max_


class TestMax(unittest.TestCase):
    def test_max_with_two_arguments(self):
        first = 1
        second = 2
        expected_result = 2

        actual_result = max_(first, second)

        self.assertEqual(actual_result, expected_result)

    def test_max_with_string(self):
        first = '1'
        second = 2

        self.assertRaises(TypeError, my_func, 'str')


unittest.main()
