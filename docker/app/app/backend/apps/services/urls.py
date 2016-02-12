"""

    services.urls
    =============

"""
from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import ServiceViewSet
from .instagram import views
# Should have the following
# post_list - a list of all publish blogs (readonly)
# post_list_all - a list of all blogs
# post_detail - if author,staff, superadmin can edit else read only
post_list = ServiceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
post_list_by_year = ServiceViewSet.as_view({
    'get': 'posts_by_year',
})
post_list_by_tag = ServiceViewSet.as_view({
    'get': 'posts_by_tag',
})
post_list_by_user = ServiceViewSet.as_view({
    'get': 'posts_by_user',
})
post_detail = ServiceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', post_list, name='list'),
    url(r'^user/(?P<user>[\w-]+)/$', post_list_by_user, name="list_user"),
    url(r'^year/(?P<year>[0-9]{4})/$', post_list_by_year, name="list_year"),
    url(r'^tag/(?P<tag>[\w-]+)/$', post_list_by_tag, name="list_tag"),
    url(r'^post/(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^post1/(?P<slug>[\w-]+)/$', post_detail, name='detail1'),
    # Instagram URLS
    url(r'^instagram/subscription_callback/', views.SubscriptionView.as_view(), name='subscription_callback'),
])