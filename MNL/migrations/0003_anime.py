# Generated by Django 3.1.3 on 2020-11-09 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MNL', '0002_delete_anime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_name', models.CharField(max_length=300)),
                ('score', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('synopsis', models.CharField(default='', max_length=500)),
                ('url', models.CharField(default='', max_length=300)),
                ('image_url', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
