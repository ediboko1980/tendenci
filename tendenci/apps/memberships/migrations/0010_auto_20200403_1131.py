# Generated by Django 2.2.10 on 2020-04-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0009_auto_20190725_1025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membershipapp',
            options={'permissions': (('view_app', 'Can view membership application'),), 'verbose_name': 'Membership Application'},
        ),
    ]
