import unittest
from typing import cast
from tests.app import App


class TestBasic(unittest.TestCase):
    def setUp(self) -> None:
        # Load test data
        self.app = App(database="./tests/integration/fixtures/test_basic.json")

    def test_customer_count(self):
        self.assertEqual(len(self.app.customers), 10)

    def test_existence_of_customer(self):
        customer = self.app.get_customer(id="CUST001")
        self.assertIsNotNone(customer)
        customer = cast(dict, customer)
        self.assertEqual(customer["name"], "John Doe")
        self.assertEqual(customer["address"], "123 Main St, New York, NY")


if __name__ == "__main__":
    unittest.main()
