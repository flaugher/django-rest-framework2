from django.contrib.auth.models import Group, User
from rest_framework import serializers

# Serializers convert a JSON object to a Django object


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize a user object.

    This uses hyperlinks instead of PKs to represent relationships.
    Hyperlinking is good RESTful design.
    See t.ly/uRK5
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """Serialize a user group object.

    This uses hyperlinks instead of PKs to represent relationships.
    See t.ly/uRK5
    """
    class Meta:
        model = Group
        fields = ['url', 'name']
