# Generated by Django 3.0.5 on 2020-04-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAC', '0009_auto_20200429_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='year',
            new_name='end_year',
        ),
        migrations.AddField(
            model_name='team',
            name='start_year',
            field=models.IntegerField(null=True),
        ),
    ]
