# Generated by Django 3.2.5 on 2021-12-27 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20211225_0554'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testchoice', models.CharField(choices=[('A', 'Test A'), ('B', 'Test B'), ('C', 'Test C')], max_length=255)),
            ],
        ),
    ]
