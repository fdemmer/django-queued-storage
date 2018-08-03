# -*- coding: utf-8 -*-
from appconf import AppConf
from django.conf import settings  # noqa


class QueuedStorageConf(AppConf):
    RETRIES = 5
    RETRY_DELAY = 60
    CACHE_PREFIX = 'queued_storage'
