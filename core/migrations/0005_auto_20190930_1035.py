# Generated by Django 2.2 on 2019-09-30 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('C', 'Cake'), ('M', 'Macaroons'), ('CC', 'Cup Cakes')], max_length=2),
        ),
    ]
