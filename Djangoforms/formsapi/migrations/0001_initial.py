# Generated by Django 2.1.4 on 2019-11-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=60)),
                ('ItemId', models.IntegerField()),
                ('ItemMail', models.EmailField(max_length=254)),
            ],
        ),
    ]
