import csv
import io

from sales.exceptions import RequestFileNameError

from .forms import UploadFileForm


def uploaded_file_data(request):
    form = UploadFileForm(request.POST, request.FILES)

    if form.is_valid():
        return handle_uploaded_file(request.FILES["file"])
    elif request.FILES.get("file") == None:
        raise RequestFileNameError()
    else:
        return []

def handle_uploaded_file(file):
    columns = ["buyer", "description", "unit_price", "quantity", "address", "provider"]

    decoded_file = file.read().decode("utf-8")
    file_reader = csv.reader(io.StringIO(decoded_file), delimiter="\t")
    next(file_reader)
    new_sales_data = [line for line in file_reader]
    data_with_columns = [zip(columns, line) for line in new_sales_data]
    payload_to_buckle = [dict(list(item)) for item in data_with_columns]

    return payload_to_buckle
