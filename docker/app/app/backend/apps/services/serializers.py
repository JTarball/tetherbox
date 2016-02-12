"""
    blog.serializers
    ================

    Serializers file for a basic Blog App

"""
from rest_framework import serializers

from project.serializers import (TagListSerializerField, TaggitSerializer)

from .models import Service


class ServiceSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Service
