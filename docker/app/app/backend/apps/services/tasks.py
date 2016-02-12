"""
    services.tasks
    ==============

    This is the main runner of the background application.

    Celery Tasks - this handles all the required tether tasks - (check triggers -> applies action where necessary)

"""
from __future__ import absolute_import

from celery import shared_task


@shared_task
def add(x, y):
    return x + y



