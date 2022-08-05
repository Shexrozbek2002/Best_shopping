# Generated by Django 4.0.6 on 2022-07-31 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinghistory',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Haridor'),
        ),
        migrations.AddField(
            model_name='shoppinghistory',
            name='product',
            field=models.ManyToManyField(to='products.cellproduct', verbose_name='Olingan Mahsulotlar'),
        ),
        migrations.AddField(
            model_name='customerpurchas',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Haridor'),
        ),
        migrations.AddField(
            model_name='customerpurchas',
            name='product',
            field=models.ManyToManyField(to='products.cellproduct', verbose_name='Olingan Mahsulotlar'),
        ),
        migrations.AddField(
            model_name='cellproduct',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Haridor'),
        ),
        migrations.AddField(
            model_name='cellproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.products', verbose_name='Sotilgan Mahsulot'),
        ),
    ]
