# Generated by Django 4.1.6 on 2023-02-08 10:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snack',
            name='state',
        ),
        migrations.AddField(
            model_name='snack',
            name='is_accepted',
            field=models.BooleanField(default=False, verbose_name='IS_ACCEPTED'),
        ),
        migrations.AlterField(
            model_name='snack',
            name='arrive_month',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)], verbose_name='ARRIVE_MONTH'),
        ),
        migrations.AlterField(
            model_name='snack',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='snack/images/', verbose_name='IMAGE'),
        ),
        migrations.AlterField(
            model_name='snack',
            name='url',
            field=models.CharField(help_text='구매 URL', max_length=400, verbose_name='URL'),
        ),
    ]
