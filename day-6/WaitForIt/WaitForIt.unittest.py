import unittest
from WaitForIt import race

class WaitForItUnitTest(unittest.TestCase):
    
    def test_race(self):
        test_answer = 4
        test_race = race()
        self.assertEqual(test_answer, test_race.determine_wins(7, 9))

    def test_multiple_races(self):
        test_answer = 288 
        test_race = race()
        self.assertEqual(test_answer, (test_race.determine_wins(7,9) * test_race.determine_wins(15, 40) * test_race.determine_wins(30, 200)))

    def test_reading_input(self):
        test_answer = [(7, 9), (15, 40), (30, 200)]
        test_race = race()
        self.assertEqual(test_answer, test_race.read_test_input("test.input"))
        for race_input in test_race.read_test_input("test.input"):
            test_race.determine_wins(*race_input)
        self.assertEqual(288, test_race.get_margin_of_error())

    def test_first_puzzle_input(self):
        test_race = race()
        for race_input in test_race.read_test_input("FirstPuzzleInput.input"):
            test_race.determine_wins(*race_input)
        self.assertEqual(32076, test_race.get_margin_of_error())

if __name__ == '__main__':
    unittest.main()
