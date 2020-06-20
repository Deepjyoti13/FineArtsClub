# Generated by Django 3.0.7 on 2020-06-20 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAC', '0012_auto_20200429_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_logo', models.ImageField(upload_to='competitions')),
                ('art_like_first', models.ImageField(upload_to='winners')),
                ('artist_like_first', models.ImageField(upload_to='artists')),
                ('name_like_first', models.CharField(max_length=50)),
                ('art_like_second', models.ImageField(upload_to='winners')),
                ('artist_like_second', models.ImageField(upload_to='artists')),
                ('name_like_second', models.CharField(max_length=50)),
                ('art_like_third', models.ImageField(upload_to='winners')),
                ('artist_like_third', models.ImageField(upload_to='artists')),
                ('name_like_third', models.CharField(max_length=50)),
                ('art_judge_first', models.ImageField(upload_to='winners')),
                ('artist_judge_first', models.ImageField(upload_to='artists')),
                ('name_judge_first', models.CharField(max_length=50)),
            ],
        ),
    ]