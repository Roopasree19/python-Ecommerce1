# Generated by Django 4.1.3 on 2022-11-15 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0002_admin_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('image', models.ImageField(max_length=255, upload_to='')),
                ('gender', models.CharField(max_length=255)),
            ],
        ),
    ]
