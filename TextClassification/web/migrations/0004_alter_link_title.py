# Generated by Django 3.2.5 on 2021-12-25 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_link_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]