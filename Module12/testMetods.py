import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Usain', speed=10)
        self.runner2 = Runner('Andrei', speed=9)
        self.runner3 = Runner('Nick', speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == 'Nick')

    def test_race_andrei_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == 'Nick')

    def test_race_usain_andrei_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == 'Nick')

if __name__ == '__main__':
    unittest.main()
