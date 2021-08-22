# Generated by Django 3.2.6 on 2021-08-18 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='user_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='idea', to='auth.user'),
            preserve_default=False,
        ),
    ]
