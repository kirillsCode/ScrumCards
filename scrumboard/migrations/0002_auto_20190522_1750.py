# Generated by Django 2.2.1 on 2019-05-22 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='business_values',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='scrumboard.List'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='story_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
