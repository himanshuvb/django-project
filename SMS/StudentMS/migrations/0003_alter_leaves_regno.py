# Generated by Django 4.0.1 on 2022-02-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentMS', '0002_leaves_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaves',
            name='regno',
            field=models.IntegerField(default=0),
        ),
    ]
