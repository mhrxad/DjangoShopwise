# Generated by Django 3.1.2 on 2020-10-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0001_initial'),
        ('products_app', '0002_auto_20201013_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='category_app.ProductCategory', verbose_name='دسته بندی ها'),
        ),
    ]