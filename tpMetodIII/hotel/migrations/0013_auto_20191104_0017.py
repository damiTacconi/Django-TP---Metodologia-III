# Generated by Django 2.2.6 on 2019-11-04 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0012_auto_20191104_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownership',
            name='cover',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]