# Generated by Django 3.2.12 on 2022-05-18 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20220518_1745'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adminhod',
            options={},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('-point', 'date')},
        ),
    ]
