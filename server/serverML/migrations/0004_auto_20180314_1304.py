# Generated by Django 2.0.2 on 2018-03-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serverML', '0003_auto_20180313_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'listPoints',
            },
        ),
        migrations.DeleteModel(
            name='MobilePoints',
        ),
    ]
