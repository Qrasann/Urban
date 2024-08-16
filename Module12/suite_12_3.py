import unittest
from testMetods import Tournament
from simpleUnitTest import Runner

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(Runner))
suite.addTests(loader.loadTestsFromTestCase(Tournament))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    runner.run(suite)
