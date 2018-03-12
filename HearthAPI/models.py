from django.db import models

from django.db import models

class Cards(models.Model):
    card_id = models.CharField(max_length=255)
    card_name = models.CharField(max_length=255)
    card_text = models.CharField(max_length=255)
    s3_image_link = models.CharField(max_length=255)

    class Meta:
        db_table = 'cards'
