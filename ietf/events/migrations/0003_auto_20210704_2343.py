# Generated by Django 2.2.19 on 2021-07-04 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210325_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='introduction',
            field=models.CharField(help_text='The introduction for the event page. Limited to 511 characters.', max_length=511),
        ),
    ]