# Generated by Django 2.2 on 2022-11-19 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20221119_1837'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bill',
            unique_together={('client_name', 'client_org', 'bill_number')},
        ),
    ]
