# Generated by Django 4.0.1 on 2022-01-11 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_alter_agendamento_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='hora',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
