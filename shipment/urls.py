from django.urls import path
from .views import ShipmentList, ShipmentDetail

urlpatterns = [
    path("", ShipmentList.as_view(), name="shipment_list"),
    path("<int:pk>/", ShipmentDetail.as_view(), name="shipment_detail"),
]
