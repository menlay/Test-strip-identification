# Generated by Django 3.1.2 on 2021-04-30 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Do_Ident', '0003_auto_20210430_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testpaper',
            name='title',
        ),
        migrations.AlterField(
            model_name='testpaper',
            name='result',
            field=models.CharField(blank=True, default=None, max_length=64),
        ),
    ]
