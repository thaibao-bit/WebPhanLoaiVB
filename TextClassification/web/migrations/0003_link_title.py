# Generated by Django 3.2.5 on 2021-12-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_link_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
