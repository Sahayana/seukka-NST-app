
# Generated by Django 4.0.3 on 2022-03-02 21:48



from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0008_alter_painting_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
