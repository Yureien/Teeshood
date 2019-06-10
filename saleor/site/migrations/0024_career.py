# Generated by Django 2.0.3 on 2019-06-10 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0023_customerbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('forms_link', models.URLField()),
                ('experience', models.CharField(max_length=40)),
                ('openings', models.IntegerField()),
                ('location', models.CharField(max_length=40)),
                ('site_settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site.SiteSettings')),
            ],
        ),
    ]