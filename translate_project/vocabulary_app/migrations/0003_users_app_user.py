# Generated by Django 4.2.6 on 2023-10-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_app', '0002_language_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='users_app_user',
            fields=[
                ('id', models.BigIntegerField(db_column='id', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='username', max_length=150)),
            ],
            options={
                'db_table': 'users_app_user',
                'managed': False,
            },
        ),
    ]
