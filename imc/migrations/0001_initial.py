# Generated by Django 2.2.6 on 2019-11-03 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.CharField(max_length=10)),
                ('estatura', models.CharField(max_length=10)),
                ('edad', models.CharField(max_length=5)),
                ('sexo', models.CharField(max_length=15)),
            ],
        ),
    ]
