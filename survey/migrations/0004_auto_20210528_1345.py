# Generated by Django 3.2.3 on 2021-05-28 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20210528_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product1',
            old_name='q1',
            new_name='p1q1',
        ),
        migrations.RenameField(
            model_name='product1',
            old_name='q2',
            new_name='p1q2',
        ),
        migrations.RenameField(
            model_name='product1',
            old_name='q3',
            new_name='p1q3',
        ),
        migrations.RenameField(
            model_name='product1',
            old_name='q4',
            new_name='p1q4',
        ),
        migrations.RenameField(
            model_name='product2',
            old_name='q1',
            new_name='p2q1',
        ),
        migrations.RenameField(
            model_name='product2',
            old_name='q2',
            new_name='p2q2',
        ),
        migrations.RenameField(
            model_name='product2',
            old_name='q3',
            new_name='p2q3',
        ),
        migrations.RenameField(
            model_name='product2',
            old_name='q4',
            new_name='p2q4',
        ),
    ]
