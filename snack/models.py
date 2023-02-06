from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Snack(models.Model):
    name = models.CharField('NAME', max_length=50, blank=False, null=False)
    image = models.ImageField('IMAGE', upload_to='snack/', blank=True, null=True)
    url = models.URLField('URL', max_length=400, help_text='구매 URL')
    description = models.CharField('DESCRIPTION', max_length=300, blank=True, help_text='간식에 대한 설명')
    state = models.CharField('STATE', max_length=50, default='waiting')
    arrive_month = models.PositiveSmallIntegerField(
        'ARRIVE_MONTH', blank=True,
        validators=[
           MaxValueValidator(12),
           MinValueValidator(1),
       ]
    )

    def __str__(self):
        return self.name
