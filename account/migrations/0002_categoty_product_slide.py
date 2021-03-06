# Generated by Django 2.0.4 on 2019-01-18 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoty',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('acprice', models.IntegerField()),
                ('discount', models.CharField(max_length=20)),
                ('disprice', models.IntegerField()),
                ('description', models.TextField()),
                ('offer', models.CharField(max_length=400)),
                ('specification', models.TextField()),
                ('seller', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
                ('categoty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Categoty')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
    ]
