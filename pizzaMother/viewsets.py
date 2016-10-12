from rest_framework import viewsets
from rest_framework import filters

from .serializers import PizzaSerializer, ToppingSerializer
from .models import Pizza, Topping

class PizzaViewSet(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', )


    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            self.queryset = self.queryset.filter(name__icontains=query)

        return self.queryset

class ToppingViewSet(viewsets.ModelViewSet):
    serializer_class = ToppingSerializer
    queryset = Topping.objects.all()
