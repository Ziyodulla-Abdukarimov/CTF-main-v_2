# Generated by Django 3.2.12 on 2022-05-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_client_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]