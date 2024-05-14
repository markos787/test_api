from rest_framework import serializers
from .models import zasadzki

class zasadzkiSerializer (serializers.ModelSerializer):
    class Meta:
        model=zasadzki
        fields='__all__'