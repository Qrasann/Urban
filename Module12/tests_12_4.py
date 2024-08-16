import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('TestRunner', speed=-5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        except Exception as e:
            logging.error("Произошла ошибка: %s", e)
            raise

    def test_run(self):
        try:
            runner = Runner(12345, speed=10)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        except Exception as e:
            logging.error("Произошла ошибка: %s", e)
            raise


if __name__ == '__main__':
    unittest.main()
