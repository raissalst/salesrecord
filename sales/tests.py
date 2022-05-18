from django.test import TestCase

from sales.models import Sale

class SaleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.buyer = 'Alan Santos'
        cls.description = 'R$300 of shirts for R$50'
        cls.unit_price = '50.0'
        cls.quantity = '6'
        cls.address = '789 Fake St'
        cls.provider = 'H&M'

        cls.new_sale = Sale.objects.create(buyer=cls.buyer, description=cls.description, unit_price=cls.unit_price, quantity=cls.quantity, address=cls.address, provider=cls.provider)
    
    def test_sale_has_information_fields(self):
        self.assertEqual(self.new_sale.buyer, self.buyer)

        self.assertEqual(self.new_sale.description, self.description)

        self.assertEqual(self.new_sale.unit_price, self.unit_price)

        self.assertEqual(self.new_sale.quantity, self.quantity)

        self.assertEqual(self.new_sale.address, self.address)

        self.assertEqual(self.new_sale.provider, self.provider)
