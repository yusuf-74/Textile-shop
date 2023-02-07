# Generated by Django 3.2.17 on 2023-02-07 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perishable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petrol', models.IntegerField()),
                ('delivery', models.IntegerField()),
                ('electricity', models.IntegerField()),
                ('water', models.IntegerField()),
                ('rent', models.IntegerField()),
                ('nails', models.IntegerField()),
                ('string', models.IntegerField()),
                ('transport', models.IntegerField()),
                ('other', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fiber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.person')),
            ],
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.person')),
            ],
        ),
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.person')),
            ],
        ),
    ]
