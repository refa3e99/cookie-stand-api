from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Shipment
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from .serializers import ShipmentSerializer


class ShipmentList(ListCreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class ShipmentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
