# Generated by Django 3.0.5 on 2024-08-31 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_category_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
