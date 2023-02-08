# Generated by Django 4.1.6 on 2023-02-08 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0006_alter_snack_description_alter_snack_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snack',
            options={'ordering': ('-modify_dt',), 'verbose_name': 'snack', 'verbose_name_plural': 'snacks'},
        ),
        migrations.AddField(
            model_name='snack',
            name='create_dt',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='CREATE_DT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snack',
            name='modify_dt',
            field=models.DateField(auto_now=True, verbose_name='MODIFY_DT'),
        ),
        migrations.AlterModelTable(
            name='snack',
            table='snack_snacks',
        ),
    ]
