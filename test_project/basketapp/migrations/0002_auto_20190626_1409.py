# Generated by Django 2.2.2 on 2019-06-26 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'корзина', 'verbose_name_plural': 'корзина'},
        ),
    ]