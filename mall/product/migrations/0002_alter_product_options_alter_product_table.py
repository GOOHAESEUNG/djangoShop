# Generated by Django 4.2.1 on 2023-05-31 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '상품', 'verbose_name_plural': '상품'},
        ),
        migrations.AlterModelTable(
            name='product',
            table='haeseung_product',
        ),
    ]
