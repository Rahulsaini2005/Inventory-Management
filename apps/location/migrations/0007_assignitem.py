# Generated by Django 3.2 on 2024-06-28 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_rename_upright_upright_aisle'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upc', models.CharField(max_length=20)),
                ('sku', models.CharField(max_length=20)),
                ('barcode_number', models.IntegerField(max_length=15, null=True)),
                ('quantity', models.IntegerField(max_length=10, null=True)),
                ('upright', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assign_item', to='location.upright')),
            ],
        ),
    ]
