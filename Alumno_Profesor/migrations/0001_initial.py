# Generated by Django 2.2.1 on 2019-07-31 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creation_date', models.DateField(auto_now=True)),
                ('delete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('correo_electronico', models.CharField(max_length=255)),
                ('creation_date', models.DateField(auto_now=True)),
                ('delete', models.BooleanField(default=False)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno_Profesor.Genero')),
            ],
            options={
                'db_table': 'Profesor',
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('correo_electronico', models.CharField(max_length=255)),
                ('creation_date', models.DateField(auto_now=True)),
                ('delete', models.BooleanField(default=False)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno_Profesor.Genero')),
            ],
            options={
                'db_table': 'Alumnos',
            },
        ),
    ]