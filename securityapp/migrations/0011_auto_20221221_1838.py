# Generated by Django 3.1.3 on 2022-12-21 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0010_booking_fromdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='booking',
            name='lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
