# Generated by Django 4.0.1 on 2022-01-18 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0005_alter_contato_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data',
            field=models.DateField(blank='True', null=True),
        ),
    ]
