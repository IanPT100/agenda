# Generated by Django 5.0.1 on 2024-01-21 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('carga_horaria', models.PositiveIntegerField()),
                ('investimento', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]