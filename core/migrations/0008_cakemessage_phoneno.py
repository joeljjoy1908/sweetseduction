# Generated by Django 2.2 on 2019-10-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191002_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='cakemessage',
            name='phoneno',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
