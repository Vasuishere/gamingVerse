# Generated by Django 5.0.6 on 2024-12-24 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_winner_winner_team_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='team_id',
        ),
    ]