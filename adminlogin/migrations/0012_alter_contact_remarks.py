# Generated by Django 4.2 on 2023-04-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlogin', '0011_alter_contact_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='remarks',
            field=models.CharField(default='', max_length=50),
        ),
    ]