# Generated by Django 4.1.6 on 2023-02-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0002_remove_snack_state_snack_is_accepted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='url',
            field=models.URLField(help_text='구매 URL', max_length=400, verbose_name='URL'),
        ),
    ]
