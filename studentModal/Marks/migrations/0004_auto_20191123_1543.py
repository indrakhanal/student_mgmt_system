# Generated by Django 2.2.3 on 2019-11-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marks', '0003_news_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AlterField(
            model_name='sixthsem',
            name='compiler',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sixthsem',
            name='dot_net',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sixthsem',
            name='e_commerce',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sixthsem',
            name='rts',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sixthsem',
            name='software',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sixthsem',
            name='webTech',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
