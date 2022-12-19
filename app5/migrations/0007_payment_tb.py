# Generated by Django 4.1.3 on 2022-11-25 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0006_remove_pro_tb_quantity_cart_tb_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app5.log_tb')),
            ],
        ),
    ]
