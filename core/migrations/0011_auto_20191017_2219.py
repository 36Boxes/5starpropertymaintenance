# Generated by Django 2.2 on 2019-10-17 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191017_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquirie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_first_name', models.CharField(max_length=100)),
                ('customer_last_name', models.CharField(max_length=100)),
                ('customer_phone_number', models.CharField(max_length=11)),
                ('job_category', models.CharField(choices=[('r', 'Roofing'), ('b', 'Brickwork'), ('d', 'Driveway'), ('p', 'Patio'), ('t', 'Turfing'), ('fs', 'Facias & Soffits '), ('g', 'Guttering'), ('fr', 'Flat Roofing'), ('pl', 'Plastering'), ('pa', 'Painting'), ('re', 'Rendering'), ('pe', 'Pebble Dashing'), ('fe', 'Fencing'), ('ex', 'Extensions')], max_length=2)),
                ('job_explanation', models.CharField(max_length=5000)),
            ],
        ),
        migrations.AlterField(
            model_name='before_and_afters',
            name='review_for_Project',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Review'),
        ),
    ]
