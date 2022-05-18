from rest_framework.exceptions import APIException


class RequestFileNameError(APIException):
    status_code = 400
    default_detail = {"message": "File name should be equal to file"}


class EmptyFileError(APIException):
    status_code = 404
    default_detail = {"message": "No sales data to record (empty text file)"}
