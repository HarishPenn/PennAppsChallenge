# Generated by Django 4.2.10 on 2024-02-09 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pennapps', '0003_alter_application_first_hackathon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='team_member_1',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='team_member_2',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='team_member_3',
            field=models.EmailField(blank=True, default='', max_length=100),
        ),
    ]
