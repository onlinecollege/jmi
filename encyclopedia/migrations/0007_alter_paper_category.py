# Generated by Django 3.2.5 on 2021-07-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0006_alter_paper_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='category',
            field=models.CharField(choices=[('Semester', 'Semester'), ('Sessional-I', 'Sessional-I'), ('Sessional-II', 'Sessional-Ii'), ('psfd', 'Psfd'), ('ksd', 'Ksd')], max_length=12),
        ),
    ]
