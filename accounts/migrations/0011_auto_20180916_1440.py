# Generated by Django 2.0.2 on 2018-09-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20180915_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='shortbio',
            field=models.TextField(default='Your bio is not updated.Please update it', max_length=183),
        ),
    ]
