import unittest
from program import utils


class TestUtils(unittest.TestCase):
    def test_reversed(self):
        self.assertEqual(utils.reversed(546), 645)
        self.assertEqual(utils.reversed(-546), -645)
        self.assertEqual(utils.reversed(54.6), 45)
        with self.assertRaises(ValueError):
            utils.formatter("hi")


    def test_formatter(self):
        self.assertEqual(utils.formatter(1), ('0b1', '0o1'))
        self.assertEqual(utils.formatter(-100), ('-0b1100100', '-0o144'))
        self.assertEqual(utils.formatter(12.34), ('0b1100', '0o14'))
        with self.assertRaises(ValueError):
            utils.formatter("hi")


if __name__ == "__main__":
    unittest.main()
