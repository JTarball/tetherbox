"""
    blog.models
    ===========

    Models file for a basic Blog App

"""
import logging
import datetime
from dateutil import relativedelta

from taggit.managers import TaggableManager

from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models, IntegrityError
from django.db.models import signals
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify

from blog.utils import markup, toTimeAgo
from search.utils import add_model_to_redis, dump_redis, flush_redis
# Get instance of logger
logger = logging.getLogger('project_logger')


class ServiceManager(models.Manager):
    use_for_related_fields = True

    def enabled(self):
        """ Returns all enabled Services. """
        return self.model.objects.filter(status=3)

    def beta(self):
        """ Returns all in-beta Services. """
        return self.model.objects.filter(status=2)

    def coming_soon(self):
        """ Returns all coming soon Services. """
        return self.model.objects.filter(status=1)

    def disabled(self):
        """ Returns all disabled Services. """
        return self.model.objects.filter(status=0)


class UserServiceManager(models.Manager):
    use_for_related_fields = True

    # def live_by_year(self, year):
    #     return self.model.objects.filter(updated_at__year=year, published=True)

    # def by_tag(self, tag):
    #     return self.model.objects.filter(tags__name__in=[tag]).distinct()

    # def live_by_tag(self, tag):
    #     return self.model.objects.filter(tags__name__in=[tag], published=True).distinct()

    def by_user(self, user):
        try:
            user_id = get_user_model().objects.get(username=user).id
        except:
            user_id = None
        return self.model.objects.filter(user_id=user_id)

    def enabled_by_user(self, user):
        try:
            user_id = get_user_model().objects.get(username=user).id
        except:
            user_id = None
        return self.model.objects.filter(user_id=user_id, service_status=3)


STATUS_CHOICES = (
    (0, 'Disabled'),
    (1, 'Coming Soon'),
    (2, 'Beta'),
    (3, 'Enabled')
)


class Service(models.Model):
    """ Service Model - A web service you can connect to. """
    # =====================
    # For Redis Search Only
    # =====================
    searchable_fields = ['name']
    # These are fields for the model which are saved to Redis. for fast access (stop gap for noSQL database)
    redis_stored_fields = ['name']
    # ======================
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    status = models.SmallIntegerField(default=0, choices=STATUS_CHOICES)  # 0=disabled, 1=coming soon, 2=beta, 3=enabled
    
    # need an image or logo
    objects = ServiceManager()



class Trigger(models.Model):
    """ A Web Trigger for a Web Service. (A Web Hook that can be checked)"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    trigger_id = models.IntegerField()  # only needs to be unique per service
    service = models.ForeignKey(Service)

    def save(self, *args, **kwargs):
        if self.model.objects().filter(trigger_id=self.trigger_id).exists():
            raise IntegrityError("There is already a trigger with id %s for service %s" % (self.trigger_id, self.service))
        super(Trigger, self).save(*args, **kwargs)


class Action(models.Model):
    """ An action that can be performed on a Web Service. """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    action_id = models.IntegerField()  # only needs to be unique per service
    service = models.ForeignKey(Service)

    def save(self, *args, **kwargs):
        if self.model.objects().filter(action_id=self.action_id).exists():
            raise IntegrityError("There is already a trigger with id %s for service %s" % (self.action_id, self.service))
        super(Trigger, self).save(*args, **kwargs)


class UserService(models.Model):
    """ UserService - What services a user is connected to. """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    token = models.CharField(max_length=255)
    service = models.ForeignKey(Service, to_field='name', related_name='+')


class Tether(models.Model):
    """ Tether - List of Web - Web Service Connections. (This is the main user web recipes). """
    trigger = models.ForeignKey(Trigger)
    actions = models.ManyToManyField(Action)
    tags = TaggableManager(blank=True)  # Give the user a useful way to describe the recipe
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    enabled = models.BooleanField(default=True, help_text=_('Designates whether the a web trigger-action is enabled.'))


##############################################################################
# Comment - type of comment (warning/ issue / comment)
##############################################################################
def reindex_redis_search(sender, instance, **kwargs):
    """ Callback function which recalculates what is searchable in redis from sender. """
    logger.info("Re-creating Search Autocomplete Index ...")
    flush_redis()
    [add_model_to_redis(model) for model in Service.objects.all()]
    dump_redis()

signals.post_save.connect(reindex_redis_search, sender=Service, dispatch_uid="add_post_tags")
