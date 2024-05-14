from django.db import models

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