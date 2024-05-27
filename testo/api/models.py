from django.db import models
from django.contrib.gis.db import models as models_gis

# Create your models here.
class zasadzki(models.Model):
    gid=models.IntegerField()
    typ=models.IntegerField()
    ranking=models.FloatField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(self.ranking, str):
            self.ranking = float(self.ranking.replace(',', '.'))

    def __str__(self):
        return f'{self.gid} - {self.typ} - {self.ranking:.2f}'
    
    class Meta:
        managed=False
        db_table='zasadzki'

class Location(models.Model):
    gid=models.IntegerField()
    typ=models.IntegerField()
    ranking=models.FloatField()
    geom=models_gis.PolygonField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if isinstance(self.ranking, str):
            self.ranking = float(self.ranking.replace(',', '.'))    

    def __str__(self):
        return f'{self.gid} - {self.typ} - {self.ranking:.2f}'
    
    class Meta:
        managed=False
        db_table='zasadzki'