# Generated by Django 3.2.17 on 2023-02-12 23:07

from django.db import migrations, models
import django.db.models.deletion
import products.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pillow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('fabric', 'fabric'), ('bag', 'bag'), ('fiber', 'fiber')], max_length=100)),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('wholesale_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('type', models.CharField(choices=[('pillow', 'pillow'), ('circular pillow', 'circular pillow')], max_length=20)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('size', models.CharField(max_length=100)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=products.utils.products_image_file_path)),
                ('bag', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.bag')),
                ('fiber', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.fiber')),
                ('fibric', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.fabric')),
            ],
        ),
        migrations.CreateModel(
            name='FiberBag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retail_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('wholesale_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('type', models.CharField(default='FiberBag', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=products.utils.products_image_file_path)),
                ('bag', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.bag')),
                ('fiber', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.fiber')),
                ('fibric', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.fabric')),
            ],
        ),
    ]