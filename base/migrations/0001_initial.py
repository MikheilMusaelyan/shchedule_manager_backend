# Generated by Django 4.1.7 on 2023-04-24 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('kontenti', models.CharField(default='', max_length=200)),
                ('ball', models.CharField(default='bal', max_length=200)),
            ],
        ),
    ]