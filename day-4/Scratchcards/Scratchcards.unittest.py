import unittest
from Scratchcards import findWinners, readCardStack

class ScratchCards(unittest.TestCase):
    
    def test_findWinners(self):
        test_my_input = [41, 48, 83, 86, 17]
        test_winning_input = {83, 86,  6, 31, 17,  9, 48, 53}
        test_answer = 4 
        self.assertEqual(test_answer, findWinners(test_my_input, test_winning_input))
    
    def test_readCardStack(self):
        test_input = 'test.input'
        test_answer = 30 
        self.assertEqual(test_answer, readCardStack(test_input))

    def test_puzzel(self):
        test_input = 'Scratchcards.input'
        test_answer = 6420979 
        self.assertEqual(test_answer, readCardStack(test_input))

if __name__ == '__main__':
    unittest.main()
