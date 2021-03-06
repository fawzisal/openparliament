# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 22:07


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='party',
            options={'verbose_name_plural': 'Parties'},
        ),
        migrations.AlterModelOptions(
            name='riding',
            options={'ordering': ('province', 'name_en')},
        ),
        migrations.RenameField(
            model_name='party',
            old_name='name',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='party',
            old_name='short_name',
            new_name='short_name_en',
        ),
        migrations.RenameField(
            model_name='riding',
            old_name='name',
            new_name='name_en',
        ),
        migrations.AddField(
            model_name='party',
            name='name_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='party',
            name='short_name_fr',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.RunSQL('UPDATE core_party SET name_fr = name_en;'),
        migrations.RunSQL('UPDATE core_party SET short_name_fr = short_name_en;'),
    ]
