# Generated by Django 2.2.6 on 2019-10-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topskills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='job_hash',
            field=models.CharField(max_length=255),
        ),
    ]
