# Generated by Django 4.0.2 on 2022-07-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview_data', '0002_alter_member_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='other_micro_controllers',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='projects',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='sensors_knowledge',
            field=models.CharField(max_length=200, null=True),
        ),
    ]