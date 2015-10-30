# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import gallery.fields.ThumbnailImageField


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=gallery.fields.ThumbnailImageField.ThumbnailImageField(upload_to='photos'),
        ),
    ]
