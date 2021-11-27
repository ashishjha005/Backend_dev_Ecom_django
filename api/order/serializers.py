from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    image=serializers.ImageField(max_length=None,allow_empty_file=False,allow_null=True,required=False)
    class Meta:
             model=Order
             fields=('user',)
             #todo add product and quantity