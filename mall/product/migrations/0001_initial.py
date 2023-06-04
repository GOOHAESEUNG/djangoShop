# Generated by Django 4.2.1 on 2023-05-31 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='상품명')),
                ('price', models.IntegerField(verbose_name='상품가격')),
                ('description', models.TextField(verbose_name='상품내용')),
                ('stuck', models.IntegerField(verbose_name='재고')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
            ],
        ),
    ]