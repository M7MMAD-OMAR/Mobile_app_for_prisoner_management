# Generated by Django 4.0.6 on 2022-07-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dungeon_Moves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dungeon_id', models.IntegerField(max_length=50000)),
                ('person_id', models.IntegerField(max_length=50000)),
                ('from_date', models.DateField(max_length=50)),
            ],
        ),
    ]
