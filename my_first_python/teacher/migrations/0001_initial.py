# Generated by Django 2.2 on 2019-04-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('teacher_id', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('joining', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=30)),
            ],
        ),
    ]
