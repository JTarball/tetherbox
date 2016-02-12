#!/usr/bin/env python
""""
    services.views
    ==============

    Danvir Guram, 2016

    views.py for Instagram Service - Here we choose a function based views for the simplicity / efficiency
"""
import logging

from .wrapper import subscriptions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import permissions

from rest_framework.views import APIView
from project.settings.base import get_env_variable

logger = logging.getLogger('project_logger')


class MyQueryParamsExpectations(serializers.Serializer):
    mode = serializers.CharField()
    challenge = serializers.CharField()
    verify_token = serializers.CharField()


class SubscriptionView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        x_hub_signature = request.header.get('X-Hub-Signature')
        raw_response = request.body.read()
        try:
            subscriptions.reactor.process(get_env_variable("INSTAGRAM_CLIENT_SECRET"), raw_response, x_hub_signature)
        except subscriptions.SubscriptionVerifyError:
            logger.error("Signature mismatch")

    def get(self, request):
        logger.debug("subscription_callback_view, request: %s" % request)
        #mode = request.GET.get("hub.mode")
        #verify_token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")
        return Response(challenge)



@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def subscription_callback_view(request):
    """ A callback url to verify subscription from Instagram. """
    logger.debug("subscription_callback_view, request: %s" % request)
    mode = request.GET.get("hub.mode")
    challenge = request.GET.get("hub.challenge")
    verify_token = request.GET.get("hub.verify_token")
    if challenge:
        return Response(challenge)
    else:
        x_hub_signature = request.header.get('X-Hub-Signature')
        raw_response = request.body.read()
        try:
            reactor.process(get_env_varible("INSTAGRAM_CLIENT_SECRET"), raw_response, x_hub_signature)
        except subscriptions.SubscriptionVerifyError:
            logger.error("Signature mismatch")
        return Response()
