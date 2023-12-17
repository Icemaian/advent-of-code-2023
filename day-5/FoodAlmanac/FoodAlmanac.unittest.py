import unittest
from FoodAlmanac import ConversionMap, Almanac
class TestConversionMap(unittest.TestCase):

    def test_convertUsingMap(self):
        test_map = ConversionMap('source', 'destination', [[50, 98, 2],[52, 50, 48]])
        test_answer = 87
        self.assertEqual(test_answer, test_map.convertUsingMap(85))

    def test_Almanac(self):
        test_alm = Almanac('test.input')
        test_answer = [82, 43, 86, 35]
        self.assertEqual(test_answer, test_alm.mapValues())
    
    def test_findMin(self):
        test_alm = Almanac('test.input')
        test_answer = 35
        test_input = test_alm.mapValues()
        self.assertEqual(test_answer, test_alm.findMin(test_input))

    def test_findMin(self):
        test_alm = Almanac('FoodAlmanac.input')
        test_answer = 35
        test_input = test_alm.mapValues()
        self.assertEqual([], test_alm.mapValues())
        self.assertEqual(test_answer, test_alm.findMin(test_input))

if __name__ == '__main__':
    unittest.main()


