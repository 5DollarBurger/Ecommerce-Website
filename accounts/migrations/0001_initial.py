# Generated by Django 3.1 on 2022-04-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('dateJoined', models.DateTimeField(auto_now_add=True)),
                ('lastLogin', models.DateTimeField(auto_now_add=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isStaff', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=False)),
                ('isSuperAdmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
