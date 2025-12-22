from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True) # ID
    model = models.CharField(max_length=200) # Modelo
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # Marca
    factory_year = models.IntegerField(blank=True, null=True) # Ano de fabricação
    model_year = models.IntegerField(blank=True, null=True) # Ano do modelo
    plate = models.CharField(max_length=10, blank=True, null=True) # Placa
    value = models.FloatField(blank=True, null=True) # Valor
    photo = models.ImageField(upload_to='cars/', blank=True, null=True) # Foto do carro

    def __str__(self):
        return self.model
