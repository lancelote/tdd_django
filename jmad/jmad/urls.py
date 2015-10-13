from django.conf.urls import include, url
from django.contrib import admin

from solos.views import SoloDetailView

urlpatterns = [
    url(r'^$', 'solos.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^recordings/(?P<album>[\w-]+)/(?P<track>[\w-]+)/(?P<artist>[\w-]+)/$',
        SoloDetailView.as_view(),
        name='solo_detail_view'
    ),
]
