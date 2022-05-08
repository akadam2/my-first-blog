# Generated by Django 4.0.2 on 2022-05-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('height', models.DecimalField(decimal_places=1, max_digits=2)),
                ('color', models.TextField(max_length=15)),
            ],
        ),
    ]
