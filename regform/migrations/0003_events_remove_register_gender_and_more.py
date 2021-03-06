# Generated by Django 4.0.3 on 2022-03-23 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regform', '0002_alter_register_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='register',
            name='gender',
        ),
        migrations.AlterField(
            model_name='register',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='regform.events'),
        ),
    ]
