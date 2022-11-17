import unittest


def max_(a, b):
    return max(a, b)


class TestMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_(1, 2), 3, 'Should be 2')

    def test_max_reverse(self):
        self.assertEqual(max_(2, 1), 2, 'Should be 2')


unittest.main()
