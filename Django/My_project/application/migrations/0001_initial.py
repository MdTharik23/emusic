# Generated by Django 5.1.3 on 2024-12-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Age', models.IntegerField(default='', max_length=20)),
                ('Address', models.CharField(default='', max_length=20)),
                ('Contact', models.IntegerField(default='', max_length=50)),
                ('Mail', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
