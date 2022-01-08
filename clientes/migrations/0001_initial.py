# Generated by Django 4.0.1 on 2022-01-08 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(blank=True, max_length=100, null=True)),
                ('telefone', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('agendado', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('observações', models.TextField()),
                ('atendente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
