# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-21 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poetryslam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inverseparticipant',
            old_name='prior_experience_if_any',
            new_name='links_to_previous_performances',
        ),
    ]
