# Generated by Django 2.0.1 on 2018-02-05 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Area', models.CharField(blank=True, max_length=30, null=True)),
                ('Tel', models.IntegerField()),
                ('age', models.IntegerField(blank=True)),
                ('DATEBIRTH', models.DateField(blank=True)),
                ('per_mess', models.TextField(blank=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='learn.User')),
            ],
        ),
    ]