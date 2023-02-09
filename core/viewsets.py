from rest_framework.viewsets import ModelViewSet

from core.models import Restaurant
from core.serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
