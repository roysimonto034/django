# Generated by Django 2.1.4 on 2019-10-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.IntegerField()),
                ('empname', models.CharField(max_length=64)),
                ('empsal', models.IntegerField()),
                ('eaddr', models.CharField(max_length=64)),
            ],
        ),
    ]
