import unittest
from own import get_average_screen


class TestAverageScreen(unittest.TestCase):
    def test_get_average_screen(self):
        self.assertEqual(get_average_screen.get_average_screen(), 0)


if __name__ == '__main__':
    unittest.main()
