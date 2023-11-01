import unittest

from app.patrat import Patrat


class TestPatrat(unittest.TestCase):
    def test_arie(self):
        patrat_1 = Patrat(4)
        expected_arie = patrat_1.get_arie()
        actual_arie = 16
        self.assertEqual(expected_arie, actual_arie)

    def test_perimetru(self):
        patrat_2 = Patrat(5)
        expected_perimetru = patrat_2.get_perimetru()
        actual_perimetru = 20
        self.assertEqual(expected_perimetru, actual_perimetru)