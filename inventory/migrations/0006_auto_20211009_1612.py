# Generated by Django 3.1.7 on 2021-10-09 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_brand_evaluation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': '库存表', 'verbose_name_plural': '库存表'},
        ),
        migrations.AddField(
            model_name='client',
            name='client_region',
            field=models.CharField(choices=[('奥地利', 'AT'), ('中国', 'CN'), ('英国', 'GB'), ('新加坡', 'SG'), ('美国', 'US'), ('委内瑞拉', 'VE')], default='', max_length=127, verbose_name='客户区域'),
        ),
        migrations.AddField(
            model_name='client',
            name='client_sex',
            field=models.CharField(choices=[('man', '男'), ('women', '女')], default='', max_length=127, verbose_name='客户性别'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='distribution_condition',
            field=models.CharField(choices=[('waiting for delivery', '等待发货'), ('transporting', '运输中'), ('to be signed', '待签收'), ('signed', '已签收')], default='', max_length=127, verbose_name='物流情况'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='evaluation_condition',
            field=models.CharField(choices=[('cannot evaluate', '未到货不可评价'), ('no evaluate', '已到货未评价'), ('have evaluated', '已评价')], default='', max_length=127, verbose_name='评价状态'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='evaluation_distribution',
            field=models.CharField(choices=[('一星评价', '*'), ('二星评价', '**'), ('三星评价', '***'), ('四星评价', '****'), ('五星评价', '*****')], default='', max_length=127, verbose_name='物流评价星数'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='evaluation_product',
            field=models.CharField(choices=[('一星评价', '*'), ('二星评价', '**'), ('三星评价', '***'), ('四星评价', '****'), ('五星评价', '*****')], default='', max_length=127, verbose_name='产品评价星数'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='evaluation_sum',
            field=models.CharField(choices=[('一星评价', '*'), ('二星评价', '**'), ('三星评价', '***'), ('四星评价', '****'), ('五星评价', '*****')], default='', max_length=127, verbose_name='总评价星数'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_condition',
            field=models.CharField(choices=[('achieved', '已完成'), ('closed', '已关闭'), ('be in progress', '进行中')], default='', max_length=127, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_address',
            field=models.CharField(max_length=40, verbose_name='客户地址'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_email',
            field=models.CharField(default='', max_length=40, verbose_name='客户邮箱'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.CharField(default='', max_length=40, primary_key=True, serialize=False, unique=True, verbose_name='客户号'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_name',
            field=models.CharField(max_length=40, verbose_name='客户名'),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_phone_number',
            field=models.CharField(max_length=40, verbose_name='客户手机号'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='distribution_order_id',
            field=models.CharField(default='', max_length=40, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_color',
            field=models.CharField(max_length=40, verbose_name='产品颜色'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_id',
            field=models.CharField(default='', max_length=40, primary_key=True, serialize=False, unique=True, verbose_name='产品号'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_name',
            field=models.CharField(max_length=40, verbose_name='产品名称'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_price',
            field=models.FloatField(verbose_name='产品单价'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_quantity',
            field=models.PositiveIntegerField(verbose_name='产品库存数量'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_size',
            field=models.CharField(default='standard', max_length=40, verbose_name='产品尺码'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_brand_id',
            field=models.CharField(max_length=40, verbose_name='品牌号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_client_id',
            field=models.CharField(max_length=40, verbose_name='客户号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_evaluate_id',
            field=models.CharField(max_length=40, verbose_name='评价号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='', max_length=40, primary_key=True, serialize=False, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_product_id',
            field=models.CharField(max_length=40, verbose_name='产品号'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_transport_id',
            field=models.CharField(max_length=40, verbose_name='运输号'),
        ),
    ]
