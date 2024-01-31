# Generated by Django 5.0.1 on 2024-01-30 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersession',
            name='user',
        ),
        migrations.AlterField(
            model_name='usersession',
            name='current_state',
            field=models.CharField(choices=[('greeting', 'Greeting'), ('question', 'Question'), ('answer', 'Answer'), ('end', 'End')], default='greeting', max_length=50),
        ),
    ]
