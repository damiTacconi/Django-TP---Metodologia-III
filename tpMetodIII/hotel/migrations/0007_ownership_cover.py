# Generated by Django 2.2.6 on 2019-11-04 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20191031_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownership',
            name='cover',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]