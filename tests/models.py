# -*- coding: utf-8 -*-
from django.db import models

from queued_storage.fields import QueuedFileField


class TestModel(models.Model):
    class Meta:
        app_label = 'tests'

    testfile = models.FileField(upload_to='test', null=True)
    remote = QueuedFileField(upload_to='test', null=True)

    retried = False
