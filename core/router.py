from rest_framework import routers

from core.viewsets import RestaurantViewSet

router = routers.DefaultRouter()
router.register('restaurants', RestaurantViewSet)
