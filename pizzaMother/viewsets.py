from rest_framework import viewsets

from .models import Pizza, Topping
from .serializers import PizzaSerializer, ToppingSerializer
from .models import Pizza, Topping

class PizzaViewSet(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()

class ToppingViewSet(viewsets.ModelViewSet):
    serializer_class = ToppingSerializer
    queryset = Topping.objects.all()
