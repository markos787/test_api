from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import zasadzki, Location

class zasadzkiSerializer (serializers.ModelSerializer):
    class Meta:
        model=zasadzki
        fields='__all__'

class LocationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model=Location
        geo_field='geom'
        fields='__all__'