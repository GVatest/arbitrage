# Generated by Django 4.1 on 2022-09-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='tg',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
