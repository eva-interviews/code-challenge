# Generated by Django 3.2.3 on 2022-01-27 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('urgency_level', models.TextField(blank=True)),
                ('body_part', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100)),
                ('type', models.TextField()),
            ],
            options={
                'db_table': 'studies',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField(null=True)),
                ('last_name', models.TextField(null=True)),
                ('birth_date', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('national_id', models.TextField(null=True)),
                ('study', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.study')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]
