# Generated by Django 4.2.1 on 2023-06-15 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='activities.activities'),
        ),
    ]
