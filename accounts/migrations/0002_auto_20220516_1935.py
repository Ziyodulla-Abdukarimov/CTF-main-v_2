# Generated by Django 3.2.12 on 2022-05-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solved',
            old_name='clent',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='answer',
            new_name='flag',
        ),
        migrations.AddField(
            model_name='task',
            name='point',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]