from django.db import models


class uch_roads(models.Model):
    sys_nom = models.IntegerField(primary_key=True)
    name_sp_roads_id = models.IntegerField()
    km = models.DecimalField(max_digits=7, decimal_places=3)
    k_km = models.DecimalField(max_digits=7, decimal_places=3)
    nomt1 = models.CharField(max_length=10)
    nomt2 = models.CharField(max_length=10)
    dl = models.DecimalField(max_digits=7, decimal_places=3)
    history = models.TextField()
    god =models.SmallIntegerField()

class sp_roads(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    km = models.DecimalField(max_digits=7, decimal_places=3)
    k_km = models.DecimalField(max_digits=7, decimal_places=3)

class kat(models.Model):
    id = models.IntegerField(primary_key=True)
    id_sp_roads = models.IntegerField()
    km = models.DecimalField(max_digits=7, decimal_places=3)
    k_km = models.DecimalField(max_digits=7, decimal_places=3)
    kat = models.CharField(max_length=3)


# Description: 	E.2.1 Номер и титул автомобильной дороги
# Name	Type	Size
# sys_nom	Длинное целое	4
# sys_nom_gis	Длинное целое	4
# name	Длинное целое	4
# km	Одинарное с плавающей точкой	4
# k_km	Одинарное с плавающей точкой	4
# nomt1	Короткий текст	10
# nomt2	Короткий текст	10
# dl	Одинарное с плавающей точкой	4
# history	Длинный текст	-
# god	Целое	2
