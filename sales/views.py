from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from sales.exceptions import EmptyFileError
from sales.models import Sale
from sales.serializers import SaleSerializer
from sales.services import uploaded_file_data


class CreateSalesView(APIView):
    def post(self, request: Request):
        data_to_buckle_received = uploaded_file_data(request)

        serializer = SaleSerializer(data=data_to_buckle_received, many=True)
        serializer.is_valid(raise_exception=True)

        if len(serializer.validated_data) == 0:
            raise EmptyFileError()

        sales = Sale.objects.bulk_create(
            [Sale(**data) for data in serializer.validated_data]
        )

        serializer = SaleSerializer(sales, many=True)

        total_gross_income = sum(
            [item.get("unit_price") * item.get("quantity") for item in serializer.data]
        )

        return Response(
            {
                "sales_data": serializer.data,
                "total gross income": f"R${total_gross_income}",
            },
            status.HTTP_201_CREATED,
        )
