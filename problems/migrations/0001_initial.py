# Generated by Django 5.2.4 on 2025-07-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeforcesContest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=100)),
                ('contest_name', models.CharField(max_length=255)),
                ('rank', models.IntegerField()),
                ('old_rating', models.IntegerField()),
                ('new_rating', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LeetcodeContest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=100)),
                ('attended_contests', models.IntegerField()),
                ('rating', models.FloatField()),
                ('global_ranking', models.IntegerField()),
                ('total_participants', models.IntegerField()),
                ('top_percentage', models.FloatField()),
            ],
        ),
    ]
