# Generated by Django 3.2.17 on 2023-02-09 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='loans',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='employees.penaltyorloans'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='penalty',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='penalty', to='employees.penaltyorloans'),
        ),
    ]