from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    phone=models.IntegerField()
    active=models.BooleanField(null=True)
    

    class Meta():
        db_table='Employee'
        verbose_name_plural='Employee'