# Generated by Django 2.0.3 on 2018-09-23 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0049_ordercomplaint_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercomplaint',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ordercomplaint',
            name='name',
        ),
    ]
