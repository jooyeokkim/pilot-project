# Generated by Django 4.1.6 on 2023-02-08 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snack', '0007_alter_snack_options_snack_create_dt_snack_modify_dt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snack',
            options={'ordering': ('-create_dt',), 'verbose_name': 'snack', 'verbose_name_plural': 'snacks'},
        ),
    ]