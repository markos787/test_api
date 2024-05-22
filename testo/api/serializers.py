from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import zasadzki, Location

class zasadzkiSerializer(serializers.ModelSerializer):
    ranking = serializers.SerializerMethodField()
    class Meta:
        model=zasadzki
        fields='__all__'

    def get_ranking(self, obj):
        return f"{obj.ranking:.2f}"

class LocationSerializer(GeoFeatureModelSerializer):
    ranking = serializers.SerializerMethodField()
    class Meta:
        model=Location
        geo_field='geom'
        fields='__all__'

    def get_ranking(self, obj):
        return f"{obj.ranking:.2f}"