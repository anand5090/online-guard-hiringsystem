# Generated by Django 3.1.3 on 2022-12-15 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardname', models.CharField(blank=True, max_length=100, null=True)),
                ('mobilenumber', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('idtype', models.CharField(blank=True, max_length=100, null=True)),
                ('idnumber', models.CharField(blank=True, max_length=100, null=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
