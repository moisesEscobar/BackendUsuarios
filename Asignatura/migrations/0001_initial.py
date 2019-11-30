# Generated by Django 2.2.1 on 2019-07-31 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alumno_Profesor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnosship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('delete', models.BooleanField(default=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno_Profesor.Alumno')),
            ],
            options={
                'db_table': 'Asignaturas_alumnos',
            },
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('hora_inicial', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('delete', models.BooleanField(default=False)),
                ('alumnos', models.ManyToManyField(related_name='asignaturas', through='Asignatura.Alumnosship', to='Alumno_Profesor.Alumno')),
            ],
            options={
                'db_table': 'Asignatura',
            },
        ),
        migrations.CreateModel(
            name='Asignaturaship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('delete', models.BooleanField(default=False)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asignatura.Asignatura')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alumno_Profesor.Profesor')),
            ],
            options={
                'db_table': 'Asignaturas_profesores',
            },
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesores',
            field=models.ManyToManyField(related_name='asignaturas', through='Asignatura.Asignaturaship', to='Alumno_Profesor.Profesor'),
        ),
        migrations.AddField(
            model_name='alumnosship',
            name='asignatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asignatura.Asignatura'),
        ),
    ]
