# Generated by Django 3.2.5 on 2021-07-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0013_auto_20210716_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='subject',
            field=models.CharField(choices=[('Isl I', 'Islamiat I'), ('Eng I', 'English I'), ('AD I', 'Animal Diversity I'), ('PD I', 'Plant Diversity I')], default='', max_length=32),
        ),
    ]
