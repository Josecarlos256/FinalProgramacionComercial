# Generated by Django 3.2.9 on 2021-11-30 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('carnet', models.CharField(max_length=10)),
                ('fechanac', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lleva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.cursos')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cursos.estudiantes')),
            ],
        ),
        migrations.AddField(
            model_name='cursos',
            name='estudiantes',
            field=models.ManyToManyField(through='cursos.Lleva', to='cursos.Estudiantes'),
        ),
    ]
