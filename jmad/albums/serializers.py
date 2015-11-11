from rest_framework import serializers

from .models import Album, Track


class AlbumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = Album


class TrackSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = Track
