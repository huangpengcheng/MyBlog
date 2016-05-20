# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_auto_20160514_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_genre',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=12, verbose_name='GenreName')),
            ],
        ),
        migrations.DeleteModel(
            name='Article_list',
        ),
        migrations.AddField(
            model_name='article',
            name='genre',
            field=models.ForeignKey(to='my_blog.Article_genre', default=123),
            preserve_default=False,
        ),
    ]
