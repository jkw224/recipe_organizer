# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default=b'This is a default description', help_text=b'This is a quick description of your recipe', null=True, blank=True)),
                ('directions', models.TextField(default=b'Add Directions', help_text=b'Steps to make the recipe')),
                ('ingredients', models.TextField(default=b'Add ingredients!', help_text=b'Ingredients to add', null=True, blank=True)),
                ('delicious', models.TextField(default=b'This is a default "this is delicious" checkbox', help_text=b'This is a quick description of your recipe', null=True, blank=True)),
                ('date_created', models.TextField(default=b'This is a default date_created', help_text=b'This is a quick description of your recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
