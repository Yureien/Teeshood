# Generated by Django 2.0.3 on 2018-08-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0064_productvariant_handle_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_pin_codes',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
