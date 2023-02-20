from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Snack(models.Model):
    name = models.CharField('NAME', max_length = 50)
    image = models.ImageField('IMAGE', upload_to = 'snack/images/')
    url = models.URLField('URL', max_length = 500)
    description = models.CharField('DESCRIPTION', max_length = 300, blank = True, help_text = ' (개수 등 설명 추가)')
    is_accepted = models.BooleanField('IS_ACCEPTED', default = False)
    supply_year = models.PositiveSmallIntegerField('SUPPLY_YEAR', default = 2023, null = True)
    supply_month = models.PositiveSmallIntegerField(
        'SUPPLY_MONTH', null = True,
        validators = [
           MaxValueValidator(12),
           MinValueValidator(1),
       ]
    )
    create_dt = models.DateField('CREATE_DT', auto_now_add = True) # 생성될 때 시각을 자동으로 기록


    class Meta:
        verbose_name = 'snack'
        verbose_name_plural = 'snacks'
        db_table = 'snack_snacks'
        ordering = ('-create_dt',)


    def __str__(self):
        return self.name
