from django.urls import path

from sales.views import CreateSalesView

urlpatterns = [
    path("upload/", CreateSalesView.as_view()),
]
