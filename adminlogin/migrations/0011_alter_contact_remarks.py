# Generated by Django 4.2 on 2023-04-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlogin', '0010_alter_contact_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]