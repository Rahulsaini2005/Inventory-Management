# Generated by Django 3.2 on 2024-06-25 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area', to='location.store'),
        ),
    ]
