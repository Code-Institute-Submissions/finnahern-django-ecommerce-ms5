# Generated by Django 4.0.3 on 2022-03-30 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
