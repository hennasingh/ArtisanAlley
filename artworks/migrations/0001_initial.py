# Generated by Django 4.2.17 on 2025-01-08 20:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artworks',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('town', models.CharField(max_length=100)),
                ('county', models.CharField(choices=[('antrim', 'Antrim'), ('armagh', 'Armagh'), ('carlow', 'Carlow'), ('cavan', 'Cavan'), ('clare', 'Clare'), ('cork', 'Cork'), ('derry', 'Derry'), ('donegal', 'Donegal'), ('down', 'Down'), ('dublin', 'Dublin'), ('fermanagh', 'Fermanagh'), ('galway', 'Galway'), ('kerry', 'Kerry'), ('kildare', 'Kildare'), ('kilkenny', 'Kilkenny'), ('laois', 'Laois'), ('leitrim', 'Leitrim'), ('limerick', 'Limerick'), ('longford', 'Longford'), ('louth', 'Louth'), ('mayo', 'Mayo'), ('meath', 'Meath'), ('monaghan', 'Monaghan'), ('offaly', 'Offaly'), ('roscommon', 'Roscommon'), ('sligo', 'Sligo'), ('tipperary', 'Tipperary'), ('tyrone', 'Tyrone'), ('waterford', 'Waterford'), ('westmeath', 'Westmeath'), ('wexford', 'Wexford'), ('wicklow', 'Wicklow')], max_length=100)),
                ('art_medium', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('tags', models.ManyToManyField(blank=True, to='artworks.tag')),
            ],
        ),
    ]
