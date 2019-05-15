from django.db import models

# Create your models here.
CarType={
    (0,'economy'),
    (1,'business'),
    (2,'first class')
}
Car={
    (0,'sedan'),
    (1,'limousine'),
    (2,'van'),
    (3,'SUV'),
    (4,'stretch limousine'),
    (5,'mini-bus')
}

class CarInformations(models.Model):
    registration_num = models.CharField(max_length=7)
    passengers_num = models.IntegerField()
    production_year = models.IntegerField()
    car_category = models.IntegerField(choices = CarType, default = 0)
    more_info = models.TextField()

class CarList(models.Model):
    producer=models.TextField()
    model = models.TextField()
    car_type = models.IntegerField(choices = Car, default = 0)
    details = models.ForeignKey('CarInformations', on_delete=models.CASCADE, blank= True)

