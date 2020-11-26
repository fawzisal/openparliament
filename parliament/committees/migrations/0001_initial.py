# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hansards', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.TextField()),
                ('short_name_en', models.TextField()),
                ('name_fr', models.TextField(blank=True)),
                ('short_name_fr', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('display', models.BooleanField(default=True, db_index=True, verbose_name=b'Display on site?')),
                ('parent', models.ForeignKey(related_name='subcommittees', blank=True, to='committees.Committee', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['name_en'],
            },
        ),
        migrations.CreateModel(
            name='CommitteeActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(max_length=500)),
                ('name_fr', models.CharField(max_length=500)),
                ('study', models.BooleanField(default=False)),
                ('committee', models.ForeignKey(to='committees.Committee', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'Committee activities',
            },
        ),
        migrations.CreateModel(
            name='CommitteeActivityInSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_id', models.IntegerField(unique=True)),
                ('activity', models.ForeignKey(to='committees.CommitteeActivity', on_delete=models.CASCADE)),
                ('session', models.ForeignKey(to='core.Session', on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeInSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acronym', models.CharField(max_length=5, db_index=True)),
                ('committee', models.ForeignKey(to='committees.Committee', on_delete=models.CASCADE)),
                ('session', models.ForeignKey(to='core.Session', on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeMeeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(db_index=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(null=True, blank=True)),
                ('source_id', models.IntegerField(null=True, blank=True)),
                ('number', models.SmallIntegerField()),
                ('minutes', models.IntegerField(null=True, blank=True)),
                ('notice', models.IntegerField(null=True, blank=True)),
                ('in_camera', models.BooleanField(default=False)),
                ('travel', models.BooleanField(default=False)),
                ('webcast', models.BooleanField(default=False)),
                ('televised', models.BooleanField(default=False)),
                ('activities', models.ManyToManyField(to='committees.CommitteeActivity')),
                ('committee', models.ForeignKey(to='committees.Committee', on_delete=models.CASCADE)),
                ('evidence', models.OneToOneField(null=True, blank=True, to='hansards.Document', on_delete=models.CASCADE)),
                ('session', models.ForeignKey(to='core.Session', on_delete=models.CASCADE)),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.SmallIntegerField(null=True, blank=True)),
                ('name_en', models.CharField(max_length=500)),
                ('name_fr', models.CharField(max_length=500, blank=True)),
                ('source_id', models.IntegerField(unique=True, db_index=True)),
                ('adopted_date', models.DateField(null=True, blank=True)),
                ('presented_date', models.DateField(null=True, blank=True)),
                ('government_response', models.BooleanField(default=False)),
                ('committee', models.ForeignKey(to='committees.Committee', on_delete=models.CASCADE)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='committees.CommitteeReport', null=True, on_delete=models.CASCADE)),
                ('session', models.ForeignKey(to='core.Session', on_delete=models.CASCADE)),
            ],
        ),
        migrations.AddField(
            model_name='committee',
            name='sessions',
            field=models.ManyToManyField(to='core.Session', through='committees.CommitteeInSession'),
        ),
        migrations.AlterUniqueTogether(
            name='committeemeeting',
            unique_together=set([('session', 'committee', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='committeeinsession',
            unique_together=set([('session', 'acronym'), ('session', 'committee')]),
        ),
        migrations.AlterUniqueTogether(
            name='committeeactivityinsession',
            unique_together=set([('activity', 'session')]),
        ),
    ]
