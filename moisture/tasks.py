# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from searches.models import Search

@shared_task
def save_search(text):
    Search(text=text).save()
