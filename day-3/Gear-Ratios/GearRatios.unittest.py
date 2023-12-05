import unittest
from GearRatios import listContainsSymbol, processLine, openData

class filenameUnitTest(unittest.TestCase):
    def test_invalidChars(self):
        test_false_input = ['.', '.', '.', '8']
        test_true_input = ['.', '.', '#', '.']
        self.assertEqual(False, listContainsSymbol(test_false_input))
    def test_processline(self):
        test_currLine = ['4','6','7','.','.','1','1','4','.','.']
        test_nextLine = ['.','.','.','*','.','.','.','.','.','.']
        test_prevLine = []
        test_answer = 467
        self.assertEqual(test_answer, processLine(test_currLine, test_nextLine, test_prevLine))
    
    def test_openData(self):
        test_input = "test.input"
        test_answer = 4361
        self.assertEqual(test_answer,openData(test_input))

    def test_puzzel(self):
        test_input = "GearRatios.input"
        test_answer = 530849
        self.assertEqual(test_answer,openData(test_input))
if __name__ == '__main__':
    unittest.main()
