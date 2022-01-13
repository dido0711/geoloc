# Generated by Django 3.1.6 on 2022-01-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='geolocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('latitude', models.CharField(max_length=16)),
                ('longitude', models.CharField(max_length=16)),
                ('accuracy', models.CharField(max_length=16)),
                ('location', models.CharField(max_length=64)),
                ('approveed', models.IntegerField(default=0)),
            ],
        ),
    ]
