import unittest, random, logging
from Trebuchet import recArrSum, lineProcessor, digitStrReplacement, loadInput
class TrebuchetUnitTest(unittest.TestCase):

    def test_recArrSum(self):
        test_input = [random.choice(range(100)) for _ in range(100)]
        test_answer = sum(test_input)
        self.assertEqual(test_answer, recArrSum(test_input), msg=f"Testing recursive Array sum function with small {test_input} and should equal {test_answer}")

    def test_lineProcessor(self):
        test_inputs = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        test_answer = [12, 38, 15, 77]
        self.assertEqual(test_answer, [lineProcessor(input) for input in test_inputs], msg=f"Testing line processor with {test_inputs}")
    def test_digitStrReplacement(self):
        test_inputs = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
        test_answer = [29, 83, 13, 24, 42, 14, 76]
        self.assertEqual(test_answer, [digitStrReplacement(input) for input in test_inputs])

    def test_loadInput(self):
        test_input = "test.input"
        test_answer = 142 
        self.assertEqual(test_answer, loadInput(test_input), msg=f"Testing Load function with small {test_input} and should equal {test_answer}")

    def test_loadInput_digitcatch(self):
        test_input = "test2.input"
        test_answer = 281 
        self.assertEqual(test_answer, loadInput(test_input, True), msg=f"Testing Load function with small {test_input} and should equal {test_answer}")

    def test_realPuzzel(self):
        test_input = "trebuchet.input"
        test_answer = 55208
        self.assertEqual(test_answer, loadInput(test_input), msg="Final Test Using Puzzel Data")

    def test_realPuzzel2(self):
        test_input = "trebuchet.input"
        test_answer = 54578
        self.assertEqual(test_answer, loadInput(test_input, True), msg="Final Test Using Puzzel Data")

if __name__ == '__main__':
    unittest.main()

