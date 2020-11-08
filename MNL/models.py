from django.db import models

# Create your models here.
class Anime(models.Model):
    anime_name = models.CharField(max_length  = 300)
    # score = models.DecimalField(max_digits = 4, decimal_places = 2,null = True)
    synopsis = models.CharField(max_length  = 500, default = '')
    url = models.CharField(max_length  = 300, default = '')
    image_url = models.CharField(max_length  = 300, default = '')
    

