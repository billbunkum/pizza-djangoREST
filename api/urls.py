from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from pizzaMother.viewsets import PizzaViewSet

router = DefaultRouter()
router.register(r'pizzas', PizzaViewSet)
#router.register(r'toppings', ToppingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]