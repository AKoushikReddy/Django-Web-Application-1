# Generated by Django 2.0.2 on 2018-09-15 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180915_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.CharField(default='Interests are not updated.Please add your Interests', max_length=80),
        ),
    ]
