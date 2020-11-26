# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('occupation', models.CharField(max_length=100, blank=True)),
                ('votetotal', models.IntegerField(null=True, blank=True)),
                ('votepercent', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('elected', models.BooleanField(null=True)),
                ('candidate', models.ForeignKey(to='core.Politician', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'Candidacies',
            },
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(db_index=True)),
                ('byelection', models.BooleanField()),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.AddField(
            model_name='candidacy',
            name='election',
            field=models.ForeignKey(to='elections.Election', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='party',
            field=models.ForeignKey(to='core.Party', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='riding',
            field=models.ForeignKey(to='core.Riding', on_delete=models.CASCADE),
        ),
    ]
