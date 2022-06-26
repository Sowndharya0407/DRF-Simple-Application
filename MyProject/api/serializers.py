from dataclasses import fields
from rest_framework import serializers
from baseApp.models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'