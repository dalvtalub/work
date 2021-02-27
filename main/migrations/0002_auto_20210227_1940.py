# Generated by Django 3.1.4 on 2021-02-27 16:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time add'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teams',
            name='logo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='logos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='matches',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.teams'),
        ),
        migrations.AlterField(
            model_name='matches',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.teams'),
        ),
    ]
