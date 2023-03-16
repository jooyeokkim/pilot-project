from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Count, Q, Case, When, FloatField, F

from user.models import User
from utils import date


class Snack(models.Model):
    name = models.CharField('NAME', max_length=50, unique=True)
    image = models.ImageField('IMAGE', upload_to='snack/images/')
    url = models.URLField('URL', max_length=500)

    class Meta:
        verbose_name = 'snack'
        verbose_name_plural = 'snacks'
        db_table = 'snack_snacks'
        ordering = ['-id']

    def __str__(self):
        return self.name


class SnackRequestQueryset(models.QuerySet):
    def order_by_like_proportion(self):
        return self.annotate(
            like=Count('id', filter=Q(snackEmotions__name="like")),
            dislike=Count('id', filter=Q(snackEmotions__name="dislike")),
            proportion=Case(
                When(
                    Q(like=0) & Q(dislike=0), then=0.5
                ),
                default=F('like') * 1.0 / (F('like') + F('dislike')),
                output_field=FloatField()
            )
        ).order_by('-proportion', '-like')


class SnackRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="snackRequests")
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE, related_name="snackRequests")
    description = models.CharField('DESCRIPTION', max_length=300, blank=True, help_text=' 예) 5개 주문해주세요!')
    is_accepted = models.BooleanField('IS_ACCEPTED', default=False)
    supply_year = models.IntegerField('SUPPLY_YEAR', null=True, blank=True, help_text=' 예) 2023')
    supply_month = models.IntegerField(
        'SUPPLY_MONTH', null=True, blank=True,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1),
        ],
        help_text=' 예) 7'
    )
    create_dt = models.DateField('CREATE_DT', auto_now_add=True)  # 생성될 때 시각을 자동으로 기록
    objects = SnackRequestQueryset.as_manager()

    @property
    def likes(self):
        return self.snackEmotions.filter(name="like").count()

    @property
    def dislikes(self):
        return self.snackEmotions.filter(name="dislike").count()


    class Meta:
        verbose_name = 'snack_request'
        verbose_name_plural = 'snack_requests'
        db_table = 'snack_snack_requests'
        ordering = ['-id']


class SnackEmotion(models.Model):
    class EmotionCategory(models.TextChoices):
        LIKE = 'like', '좋아요'
        DISLIKE = 'dislike', '싫어요'

    name = models.CharField('name', max_length=50, choices=EmotionCategory.choices) # type 변수이름
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="snackEmotions")
    snack_request = models.ForeignKey(SnackRequest, on_delete=models.CASCADE, related_name="snackEmotions")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'snack_request'], name='user_snack_request_unique_constraint')
        ]
