import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def freeze_check(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest('Тесты в этом кейсе заморожены')
            return func(self, *args, **kwargs)
        return wrapper

    @freeze_check
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == 'Nick')

    @freeze_check
    def test_race_andrei_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == 'Nick')

    @freeze_check
    def test_race_usain_andrei_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last_place = max(self.all_results)
        self.assertTrue(self.all_results[last_place] == 'Nick')

if __name__ == '__main__':
    unittest.main()
