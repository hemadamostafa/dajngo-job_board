# Generated by Django 3.1 on 2020-08-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=' ', max_length=1000),
            preserve_default=False,
        ),
    ]
