import unittest


def max_(a, b):
    if a > b:
        return a

    return b


class TestMax(unittest.TestCase):
    def test_max_with_two_arguments(self):
        first = 1
        second = 2
        expected_result = 2

        actual_result = max_(first, second)
        self.assertEqual(actual_result, expected_result)

    def test_max_with_three_arguments(self):
        first = 1
        second = 2
        third = 3
        expected_result = 3

        # actual_result = max_(first, second, third)
        # self.assertEqual(actual_result, expected_result)

        with self.assertRaises(TypeError):
            actual_result = max_(first, second, third)


if __name__ == '__main__':
    unittest.main()
