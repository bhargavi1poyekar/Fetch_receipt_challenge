import unittest
from app.services.receipt_service import (
    points_from_retailer_name,
    points_from_round_total,
    points_from_multiple_of_25,
    points_from_item_count,
    points_from_item_description,
    points_from_purchase_date,
    points_from_purchase_time,
    generate_receipt_id
)

class TestReceiptService(unittest.TestCase):

    def test_points_from_retailer_name(self):
        self.assertEqual(points_from_retailer_name("Walmart123"), 10)
        self.assertEqual(points_from_retailer_name("!@#$"), 0)

    def test_points_from_round_total(self):
        self.assertEqual(points_from_round_total("20.00"), 50)
        self.assertEqual(points_from_round_total("19.99"), 0)

    def test_points_from_multiple_of_25(self):
        self.assertEqual(points_from_multiple_of_25("20.25"), 25)
        self.assertEqual(points_from_multiple_of_25("19.99"), 0)

    def test_points_from_item_count(self):
        self.assertEqual(points_from_item_count([{}, {}]), 5)
        self.assertEqual(points_from_item_count([{}]), 0)

    def test_points_from_item_description(self):
        items = [{'shortDescription': '  ABC  ', 'price': '10.00'}]
        self.assertEqual(points_from_item_description(items), 2)

    def test_points_from_purchase_date(self):
        self.assertEqual(points_from_purchase_date("2023-09-01"), 6)  # Odd date
        self.assertEqual(points_from_purchase_date("2023-09-02"), 0)  # Even date

    def test_points_from_purchase_time(self):
        self.assertEqual(points_from_purchase_time("14:30"), 10)  # 2:30 PM
        self.assertEqual(points_from_purchase_time("16:01"), 0)  # 4:01 PM

    def test_generate_receipt_id(self):
        id1 = generate_receipt_id()
        id2 = generate_receipt_id()
        self.assertNotEqual(id1, id2) # IDs should be unique


if __name__ == '__main__':
    unittest.main()
