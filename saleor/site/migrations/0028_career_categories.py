# Generated by Django 2.0.3 on 2019-06-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0027_remove_career_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='categories',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
