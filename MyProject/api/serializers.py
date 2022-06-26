from dataclasses import fields
from rest_framework import serializers
from baseApp.models import *
# this is for serizlizer
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
