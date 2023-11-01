import unittest

import HtmlTestRunner

from tests.test_cerc import TestCerc
from tests.test_patrat import TestPatrat


class UnitTests(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCerc),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPatrat)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Unit Tests Results',
            report_name='unittests_report'
        )
        runner.run(teste_de_rulat)