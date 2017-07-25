# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-08 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=140)),
                ('unit', models.CharField(choices=[('KG', 'KG'), ('gm', 'gm')], default='KG', max_length=2)),
                ('image', models.ImageField(upload_to='prod_images/')),
                ('writeup', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'master_products',
            },
        ),
        migrations.CreateModel(
            name='Product_bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket', models.CharField(choices=[('Base', 'Base'), ('Curry', 'Curry'), ('Thooran', 'Thooran')], default='Base', max_length=40)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product')),
            ],
            options={
                'db_table': 'product_bucket',
            },
        ),
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Home Grown', 'Home Grown'), ('Ooty Special', 'Ooty Special'), ('Organic', 'Organic')], default='Organic', max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_qty', models.DecimalField(decimal_places=2, max_digits=2)),
                ('avlb_qty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='prod_images/')),
                ('writeup', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Product')),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
        migrations.AlterUniqueTogether(
            name='product_category',
            unique_together=set([('name', 'category')]),
        ),
    ]