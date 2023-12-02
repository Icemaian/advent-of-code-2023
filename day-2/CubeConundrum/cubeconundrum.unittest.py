import unittest
from CubeConundrum import CubeGame, findPossibleGames, findMinSetPowered

class CubeGameUnitTest(unittest.TestCase):
    def test_init(self):
        test_input = "Game 1: 10 green, 9 blue, 1 red; 1 red, 7 green"
        test_answer = {
            'id': 1,
            'rounds': ['round1', 'round2'],
            'maxTypeObsv': {'green': 10, 'blue': 9, 'red': 1}
        }
        newGame = CubeGame(test_input)
        self.assertEqual(test_answer['id'], newGame.id)
        self.assertEqual(len(test_answer['rounds']), len(newGame.rounds))
        self.assertEqual(test_answer['maxTypeObsv'], newGame.maxTypeObsv)

    def test_isPossible(self):
        test_class_input = "Game 1: 10 green, 9 blue, 1 red; 1 red, 7 green"
        test_false_input = {'red': 1, 'blue': 5, 'green': 10}
        test_true_input = {'red': 1, 'blue': 14, 'green': 10}
        test_answer = [False, True]
        newGame = CubeGame(test_class_input)
        self.assertEqual(test_answer[0], newGame.isPossible(test_false_input))
        self.assertEqual(test_answer[1], newGame.isPossible(test_true_input))

    def test_findPossibleGames(self):
        test_input = {'red': 12, 'blue': 14, 'green': 13}
        test_answer = 8
        self.assertEqual(test_answer, findPossibleGames("test.input", test_input))

    def test_puzzel(self):
        test_input = {'red': 12, 'blue': 14, 'green': 13}
        test_answer = 2239
        self.assertEqual(test_answer, findPossibleGames("cubeconundrum.input", test_input))

    def test_findMinSetPowered(self):
        test_answer = 2286
        self.assertEqual(test_answer, findMinSetPowered("test.input"))

    def test_puzzel(self):
        test_answer = 83435
        self.assertEqual(test_answer, findMinSetPowered('cubeconundrum.input'))

if __name__ == '__main__':
    unittest.main()
