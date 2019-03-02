# Generated by Django 2.1.7 on 2019-02-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='image',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='category',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]