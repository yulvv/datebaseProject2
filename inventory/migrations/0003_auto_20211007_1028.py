# Generated by Django 3.1.7 on 2021-10-07 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(default='', max_length=40, primary_key=True, serialize=False, unique=True, verbose_name='Order ID')),
                ('order_product_id', models.CharField(max_length=40, verbose_name='Product ID')),
                ('order_brand_id', models.CharField(max_length=40, verbose_name='Brand ID')),
                ('order_transport_id', models.CharField(max_length=40, verbose_name='Transport ID')),
                ('order_evaluate_id', models.CharField(max_length=40, verbose_name='Evaluate ID')),
                ('order_client_id', models.CharField(max_length=40, verbose_name='Client ID')),
                ('order_purchase_quantity', models.PositiveIntegerField(verbose_name='Purchase Quantity')),
                ('order_aggregate_amount', models.FloatField(verbose_name='Aggregate Amount')),
            ],
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_quantity',
            field=models.PositiveIntegerField(verbose_name='Product Quantity'),
        ),
    ]
