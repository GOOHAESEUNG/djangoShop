# Generated by Django 4.2.1 on 2023-05-31 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='haeseung_user',
        ),
    ]