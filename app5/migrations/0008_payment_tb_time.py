# Generated by Django 4.1.3 on 2022-11-25 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0007_payment_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_tb',
            name='time',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
