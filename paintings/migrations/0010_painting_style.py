# Generated by Django 4.0.3 on 2022-03-02 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0009_alter_user_options_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='style',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
