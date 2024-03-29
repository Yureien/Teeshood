# Generated by Django 2.0.3 on 2018-10-22 12:13

from django.db import migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0050_auto_20180923_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount_amount',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_price_gross',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, default=0, editable=False, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_price_net',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, default=0, editable=False, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_gross',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_net',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='unit_price_gross',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='unit_price_net',
            field=django_prices.models.MoneyField(currency='INR', decimal_places=2, max_digits=12),
        ),
    ]
