from io import StringIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase
from rest_framework.test import APITestCase

from sales.models import Sale


class SaleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.buyer = "Alan Santos"
        cls.description = "R$300 of shirts for R$50"
        cls.unit_price = "50.0"
        cls.quantity = "6"
        cls.address = "789 Fake St"
        cls.provider = "H&M"

        cls.new_sale = Sale.objects.create(
            buyer=cls.buyer,
            description=cls.description,
            unit_price=cls.unit_price,
            quantity=cls.quantity,
            address=cls.address,
            provider=cls.provider,
        )

    def test_sale_has_correct_information_fields(self):
        self.assertEqual(self.new_sale.buyer, self.buyer)

        self.assertEqual(self.new_sale.description, self.description)

        self.assertEqual(self.new_sale.unit_price, self.unit_price)

        self.assertEqual(self.new_sale.quantity, self.quantity)

        self.assertEqual(self.new_sale.address, self.address)

        self.assertEqual(self.new_sale.provider, self.provider)


class MyTestCase(APITestCase):
    @classmethod
    def setUpTextFile(cls):
        io = StringIO(
            "Comprador\tDescrição\tPreço Unitário\tQuantidade\tEndereço\tFornecedor\nJoão Silva\tR$10 of R$20 of food\t10.0\t2\t987 Fake St\tBobs"
        )
        io.write("foo")

        text_file = InMemoryUploadedFile(
            io, None, "foo.txt", "text", io.line_buffering, charset="utf-8"
        )
        text_file.seek(0)
        return text_file

    def setEmptyFile(cls):
        io = StringIO()
        io.write("empty")

        text_file = InMemoryUploadedFile(
            io, None, "empty.txt", "text", io.line_buffering, charset="utf-8"
        )
        text_file.seek(0)
        return text_file

    def test_upload_text_file(self):
        test_file = self.setUpTextFile()

        response = self.client.post(
            "/api/upload/",
            {
                "file": test_file,
            },
            format="multipart",
        )
        self.assertEqual(response.status_code, 201)

    def test_upload_text_file_with_wrong_name_field_in_request(self):
        test_file = self.setUpTextFile()

        response = self.client.post(
            "/api/upload/",
            {
                "text": test_file,
            },
            format="multipart",
        )

        output = response.json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(output, {"message": "File name should be equal to file"})

    def test_upload_text_file_with_no_data(self):
        test_file = self.setEmptyFile()

        response = self.client.post(
            "/api/upload/",
            {
                "file": test_file,
            },
            format="multipart",
        )

        output = response.json()

        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            output, {"message": "No sales data to record (empty text file)"}
        )
