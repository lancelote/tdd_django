from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from albums.views import AlbumViewSet

router = routers.SimpleRouter()
router.register(r'albums', AlbumViewSet)

urlpatterns = [
    # API
    url(r'^api/', include(router.urls)),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Apps
    url(r'^$', 'solos.views.index'),
    url(
        r'^recordings/(?P<album>[\w-]+)/(?P<track>[\w-]+)/(?P<artist>[\w-]+)/$',
        'solos.views.solo_detail',
        name='solo_detail_view'
    ),
]
