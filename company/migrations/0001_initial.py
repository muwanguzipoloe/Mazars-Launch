# Generated by Django 2.0.3 on 2018-04-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=122, null=True)),
                ('designation', models.CharField(blank=True, max_length=122, null=True)),
                ('company', models.CharField(blank=True, max_length=122, null=True)),
                ('status', models.CharField(blank=True, max_length=122, null=True)),
                ('date_of_update', models.DateField(blank=True, null=True)),
                ('response', models.CharField(blank=True, max_length=122, null=True)),
                ('telephone_contact', models.IntegerField(blank=True, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
