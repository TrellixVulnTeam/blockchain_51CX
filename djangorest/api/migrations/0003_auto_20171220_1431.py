# Generated by Django 2.0 on 2017-12-20 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='proof_of_work',
            field=models.IntegerField(blank=True, default=0, unique=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='block',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Block'),
        ),
    ]