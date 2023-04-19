# Generated by Django 4.2 on 2023-04-17 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_rename_place_tournoi_location_alter_tournoi_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name of the team')),
                ('coach_name', models.CharField(max_length=200, verbose_name='Name of the coach')),
            ],
        ),
        migrations.CreateModel(
            name='Poule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_number', models.IntegerField(verbose_name='Pool number')),
                ('teams', models.ManyToManyField(to='tournaments.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournoi', verbose_name='Tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.team', verbose_name='Team')),
            ],
        ),
    ]