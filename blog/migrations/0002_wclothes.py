# Generated by Django 4.2.6 on 2024-01-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wclothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='Wclothes/img')),
                ('seller', models.CharField(max_length=100)),
            ],
        ),
    ]
