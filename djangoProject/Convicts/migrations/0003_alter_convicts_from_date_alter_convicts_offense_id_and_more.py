# Generated by Django 4.0.6 on 2022-07-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Convicts', '0002_alter_convicts_offense_id_alter_convicts_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convicts',
            name='from_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='convicts',
            name='offense_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='convicts',
            name='person_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='convicts',
            name='to_date',
            field=models.DateField(),
        ),
    ]