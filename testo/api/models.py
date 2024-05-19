from django.db import models
from django.contrib.gis.db import models as models_gis

# Create your models here.
class zasadzki(models.Model):
    gid=models.TextField()
    typ=models.TextField()
    ranking=models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        managed=False
        db_table='zasadzki'

class Location(models.Model):
    gid=models.TextField()
    typ=models.TextField()
    ranking=models.TextField()
    geom=models_gis.PolygonField()

    def __str__(self):
        return self.title
    
    class Meta:
        managed=False
        db_table='zasadzki'