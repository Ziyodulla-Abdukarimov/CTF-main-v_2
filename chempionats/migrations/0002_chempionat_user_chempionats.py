# Generated by Django 3.2.13 on 2022-07-11 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chempionats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chempionat_user',
            name='chempionats',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chempionats.chempionats'),
            preserve_default=False,
        ),
    ]
