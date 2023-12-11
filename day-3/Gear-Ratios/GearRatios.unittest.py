import unittest
from GearRatios import listContainsSymbol, processLine, openData, gearValue, findGear

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
        self.assertEqual(test_answer,openData(test_input)[0])

    def test_puzzel(self):
        test_input = "GearRatios.input"
        test_answer = 530849
        self.assertEqual(test_answer,openData(test_input)[0])

    def test_gearValue(self):
        test_input = (['7','7','.','1','1','4','.'], 2)
        test_answer = [77,114]
        self.assertEqual(test_answer, gearValue(test_input[0], test_input[1]))
    
    def test_findGear(self):
        test_currLine = list('...........*...................638..72...........+......367........802.........&..............=....*..*................-.../....401.773.....')
        test_nextLine = list('........535...................*............4.29..........*.....784*....526........................141.342.189........630..958...............')
        test_prevLine = list('...........2.235*..........*..........*318.......317............................383.567..705.923..716.409.68.......................*........')
        test_answer = 241904 
        self.assertEqual(test_answer, findGear(test_currLine, test_nextLine, test_prevLine))
    
    def test_openData(self):
        test_input = 'test.input'
        test_answer = 467835
        self.assertEqual(test_answer, openData(test_input)[1])

    def test_finalPuzzel(self):
        test_input = 'GearRatios.input'
        test_answer = 84900879
        self.assertEqual(test_answer, openData(test_input)[1])

if __name__ == '__main__':
    unittest.main()
