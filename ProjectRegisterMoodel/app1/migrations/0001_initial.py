# Generated by Django 2.2.24 on 2022-04-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuID', models.IntegerField()),
                ('stuName', models.CharField(max_length=100)),
                ('stuAddr', models.CharField(max_length=100)),
                ('stuPass', models.CharField(max_length=100)),
                ('stuComment', models.CharField(max_length=100)),
                ('stuMobno', models.IntegerField()),
            ],
        ),
    ]