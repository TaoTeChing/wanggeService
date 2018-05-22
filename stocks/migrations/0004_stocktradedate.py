# Generated by Django 2.0.4 on 2018-05-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20180518_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='stocktradedate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradedate', models.DateField(unique=True, verbose_name='交易日期')),
            ],
            options={
                'verbose_name': 'A股交易日',
            },
        ),
    ]