import unittest
from src.Stats import StatisticsSystem


class TestStatisticsSystem(unittest.TestCase):

    def setUp(self):
        """Runs before each test"""
        self.system = StatisticsSystem("data.csv")

    # Test file validation
    def test_validate_file_name(self):
        self.assertTrue(self.system.validate_file_name())

    # Test mean calculation
    def test_mean(self):
        self.system.weights = [10, 20, 30]
        self.assertEqual(self.system.get_mean(), 20.0)

    # Test median (odd case)
    def test_median_odd(self):
        self.system.weights = [10, 20, 30]
        self.assertEqual(self.system.get_median(), 20.0)

    # Test median (even case)
    def test_median_even(self):
        self.system.weights = [10, 20, 30, 40]
        self.assertEqual(self.system.get_median(), 25.0)

    # Test mode (basic check)
    def test_mode(self):
        self.system.weights = [80, 80, 90, 100]
        mode = self.system.get_mode()
        self.assertTrue(mode > 0)


if __name__ == "__main__":
    unittest.main()