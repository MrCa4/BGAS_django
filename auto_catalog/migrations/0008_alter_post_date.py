# Generated by Django 4.1.1 on 2022-10-05 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_catalog', '0007_alter_post_date_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 5, 16, 57, 50, 344524)),
        ),
    ]
