# Generated by Django 5.1.4 on 2025-01-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
