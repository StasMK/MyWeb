# Generated by Django 3.2.5 on 2021-08-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_sp_roads', models.IntegerField()),
                ('km', models.DecimalField(decimal_places=3, max_digits=7)),
                ('k_km', models.DecimalField(decimal_places=3, max_digits=7)),
                ('kat', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='sp_roads',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('km', models.DecimalField(decimal_places=3, max_digits=7)),
                ('k_km', models.DecimalField(decimal_places=3, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='uch_roads',
            fields=[
                ('sys_nom', models.IntegerField(primary_key=True, serialize=False)),
                ('name_sp_roads_id', models.IntegerField()),
                ('km', models.DecimalField(decimal_places=3, max_digits=7)),
                ('k_km', models.DecimalField(decimal_places=3, max_digits=7)),
                ('nomt1', models.CharField(max_length=10)),
                ('nomt2', models.CharField(max_length=10)),
                ('dl', models.DecimalField(decimal_places=3, max_digits=7)),
                ('history', models.TextField()),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('data_greated', models.DateTimeField(auto_now_add=True)),
                ('data_update', models.DateTimeField(auto_now=True)),
                ('god', models.SmallIntegerField()),
            ],
        ),
    ]
