# Generated by Django 5.0 on 2023-12-21 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salespersons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesperson',
            name='pic',
            field=models.ImageField(default='', upload_to='customers'),
        ),
    ]
