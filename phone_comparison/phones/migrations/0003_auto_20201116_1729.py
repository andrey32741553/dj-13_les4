# Generated by Django 3.1.2 on 2020-11-16 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_specialproperties'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialproperties',
            name='phone_name',
        ),
        migrations.AddField(
            model_name='phone',
            name='special',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phones.specialproperties'),
        ),
    ]
