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
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    data_greated = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
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

# 13