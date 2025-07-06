import unittest
from main import bubble_sort

class TestAddNumbers(unittest.TestCase):

    def test_already_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()