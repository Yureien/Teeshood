# Generated by Django 2.0.3 on 2018-09-23 11:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0048_ordercomplaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercomplaint',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
