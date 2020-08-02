from django.db import models

class Device(models.Model):
    type=models.CharField(max_length=30,blank=False)
    price=models.FloatField()
    choices=(
        ('AVAILABLE','Items ready to be purchase'),
        ('SOLD','Item sold'),
        ('RESTOCKING','Restocking item in a few days')
    )
    status=models.CharField(max_length=10, choices=choices,default="Sold")
    issue=models.CharField(max_length=100,default="No issues")

    class Meta:
        abstract=True

    def __str__(self):
        return  self.type


class Laptop(Device):
    pass
class Mobile(Device):
    pass

class Desktop(Device):
    pass
