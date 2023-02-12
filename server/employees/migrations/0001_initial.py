# Generated by Django 3.2.17 on 2023-02-09 13:47


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PenaltyOrLoans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_debt', models.CharField(choices=[('penalty', 'penalty'), ('loans', 'loans')], max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('customer', 'customer'), ('employee', 'employee'), ('supplier', 'supplier')], default='employee', max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('government', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_hours', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('num_of_days', models.IntegerField()),
                ('salry_per_hour', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('loans', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='employees.penaltyorloans')),
                ('penalty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='penalty', to='employees.penaltyorloans')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='salary', to='employees.person')),
            ],
        ),
    ]
