from rest_framework import serializers

from .models import Pizza, Topping


#encode attributes from a model into a dictionary 
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'base_price', 'created', )
        read_only_fields = ('id', 'base_price', 'created', )

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name', 'price', )

#what needs to be encoded here?