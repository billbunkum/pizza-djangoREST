from rest_framework import serializers

from .models import Pizza, Topping


#encode attributes from a model into a dictionary 
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('id', 'name', 'base_price', 'created', 'total_price', )
        read_only_fields = ('id', 'base_price', 'created', 'total_price', )

    # total_price = serializers.SerializerModelField()
        # creates a def get_
    # def get_total_price(self, obj):
    #     total_price = obj.base_price

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name', 'price', )

#what needs to be encoded here?