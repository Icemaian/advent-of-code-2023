import unittest, random
from Trebuchet import recArrSum, lineProcessor, loadInput
class TrebuchetUnitTest(unittest.TestCase):

    def test_recArrSum(self):
        test_input = [random.choice(range(100)) for _ in range(100)]
        test_answer = sum(test_input)
        self.assertEqual(test_answer, recArrSum(test_input))

    def test_lineProcessor(self):
        test_inputs = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        test_answer = [12, 38, 15, 77]
        self.assertEqual(test_answer, [lineProcessor(input) for input in test_inputs])

    def loadInput(self):
        test_input = "test.input"
        test_answer = 77
        self.assertEqual(test_answer, loadInput())

if __name__ == '__main__':
    unittest.main()

