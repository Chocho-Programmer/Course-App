# Generated by Django 4.2 on 2023-04-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='alias',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
