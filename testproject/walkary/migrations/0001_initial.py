# Generated by Django 5.1.2 on 2024-11-11 05:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('gender', models.CharField(blank=True, choices=[('男性', '男性'), ('女性', '女性'), ('その他', 'その他')], max_length=20)),
                ('goal', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
