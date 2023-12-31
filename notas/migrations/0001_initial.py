# Generated by Django 4.2.3 on 2023-07-06 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50, unique=True)),
                ('ci', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura_Semestre_Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.asignatura')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.estudiante')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.semestre')),
            ],
        ),
    ]
