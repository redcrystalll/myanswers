import unittest
from find_matching_pair import find_matching_pair

class TestFindMatchingPair(unittest.TestCase):

    def test_find_matching_pair(self):
        numbers = [2, 3, 6, 7]
        target_sum = 9
        expected_result = (3, 6)
        result = find_matching_pair(numbers, target_sum)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
