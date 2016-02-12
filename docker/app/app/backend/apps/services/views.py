'''
    blog.views
    ==========
    Note: As Django is only used as a backend there are no
           template based views. All views are ajax views
           returning json objects of models.
'''
import logging

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route

from project.permissions import IsAdminOrReadOnly

from .models import Service
from .serializers import ServiceSerializer

logger = logging.getLogger('project_logger')


class ServiceViewSet(viewsets.ModelViewSet):
    """
        Gets/Updates/Deletes a single or list of posts.
        This viewset automatically provides `list`, `create`, `retrieve`,`update` and `destroy` actions.
        Additionally we also provide an extra `posts_by_year` and `posts_by_user` action.
    """
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminOrReadOnly, )
    lookup_field = 'slug'

    @list_route(methods=['get'])
    def posts_by_year(self, request, *args, **kwargs):
        """
            Returns a list of posts from a given year.
        """
        if self.request.user.is_staff or self.request.user.is_superuser:
            posts = Service.objects.by_year(kwargs['year'])
        else:
            posts = Service.objects.live_by_year(kwargs['year'])
        serializer = ServiceSerializer(posts, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def posts_by_tag(self, request, *args, **kwargs):
        """
            Returns a list of posts from a given tag.
        """
        if self.request.user.is_staff or self.request.user.is_superuser:
            posts = Service.objects.by_tag(kwargs['tag'])
        else:
            posts = Service.objects.live_by_tag(kwargs['tag'])
        serializer = ServiceSerializer(posts, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def posts_by_user(self, request, *args, **kwargs):
        """
            Returns a list of posts for a given author.
        """
        if self.request.user.is_staff or self.request.user.is_superuser:
            posts = Service.objects.by_user(kwargs['user'])
        else:
            posts = Service.objects.live_by_user(kwargs['user'])
        serializer = ServiceSerializer(posts, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Service.objects.all()
        else:
            # logger.warn("live post call only")
            return Service.objects.live()
