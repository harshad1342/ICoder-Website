# Generated by Django 3.0.4 on 2020-03-31 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200331_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
