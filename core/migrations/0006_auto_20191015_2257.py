# Generated by Django 2.2 on 2019-10-15 22:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191015_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='before_and_afters',
            name='job_date',
        ),
        migrations.AddField(
            model_name='before_and_afters',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
