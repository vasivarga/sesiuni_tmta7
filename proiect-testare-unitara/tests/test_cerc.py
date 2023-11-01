import unittest

from app.cerc import Cerc


class TestCerc(unittest.TestCase):

    def test_arie(self):
        cerc_1 = Cerc(5)
        expected_arie = cerc_1.get_arie()
        actual_arie = 78.5
        self.assertEqual(expected_arie, actual_arie)

    def test_diametru(self):
        cerc_2 = Cerc(6)
        expected_diametru = cerc_2.get_diametru()
        actual_diametru = 12
        self.assertEqual(expected_diametru, actual_diametru)

