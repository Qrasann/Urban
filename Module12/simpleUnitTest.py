import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def freeze_check(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest('Тесты в этом кейсе заморожены')
            return func(self, *args, **kwargs)
        return wrapper

    @freeze_check
    def test_walk(self):
        runner = Runner('TestRunner')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @freeze_check
    def test_run(self):
        runner = Runner('TestRunner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @freeze_check
    def test_challenge(self):
        runner1 = Runner('TestRunner1')
        runner2 = Runner('TestRunner2')
        for _ in range(10):
            runner1.run()
            runner1.walk()
        for _ in range(3):
            runner2.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    unittest.main()
