# Generated by Django 3.0.8 on 2020-07-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200706_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='starred',
            field=models.BooleanField(default=False),
        ),
    ]
