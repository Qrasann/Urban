import unittest
from testMetods import TournamentTest
from simpleUnitTest import RunnerTest

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    runner.run(suite)
