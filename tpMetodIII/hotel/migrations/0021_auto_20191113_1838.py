# Generated by Django 2.2.6 on 2019-11-13 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0020_auto_20191113_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentaldate',
            name='booked',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hotel.Book'),
        ),
    ]
