# Generated by Django 4.2.10 on 2024-02-08 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pennapps', '0002_application_birthday_application_first_hackathon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='first_hackathon',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], default='b', max_length=1),
        ),
        migrations.AlterField(
            model_name='application',
            name='year',
            field=models.CharField(choices=[('nth', 'Ninth Grade'), ('ten', 'Tenth Grade'), ('ele', 'Eleventh Grade'), ('twl', 'Twelfth Grade'), ('fr', 'Freshman'), ('so', 'Sophomore'), ('ju', 'Junior'), ('se', 'Senior'), ('gr', 'Grad')], default='nth', max_length=3),
        ),
    ]
