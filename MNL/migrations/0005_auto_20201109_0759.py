# Generated by Django 3.1.3 on 2020-11-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MNL', '0004_auto_20201109_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='synopsis',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
