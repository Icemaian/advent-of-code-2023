import unittest
from GearRatios import listContainsSymbol

class filenameUnitTest(unittest.TestCase):
    def test_invalidChars(self):
        test_false_input = ['.', '.', '.', '8']
        test_true_input = ['.', '.', '#', '.']
        self.assertEqual(False, listContainsSymbol(test_false_input))
        self.assertEqual(True, listContainsSymbol(test_true_input))


if __name__ == '__main__':
    unittest.main()
