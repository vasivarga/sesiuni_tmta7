import unittest

import HtmlTestRunner

from tests.test_api_status import TestApiStatus
from tests.test_delete_order import TestDeleteOrder
from tests.test_get_order import TestGetOrder
from tests.test_list_of_books import TestListOfBooks
from tests.test_submit_order import TestSubmitOrder
from tests.test_update_order import TestUpdateOrder


class TestSuite(unittest.TestCase):

    def test_suite(self):

        suita_de_teste = unittest.TestSuite()

        suita_de_teste.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestApiStatus),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestListOfBooks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateOrder),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteOrder)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="API Test Report",
            report_name="Books API Test Results"
        )

        runner.run(suita_de_teste)
