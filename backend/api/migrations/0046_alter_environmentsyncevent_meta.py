# Generated by Django 4.2.7 on 2023-11-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_alter_environmentsync_service_environmentsyncevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmentsyncevent',
            name='meta',
            field=models.JSONField(null=True),
        ),
    ]