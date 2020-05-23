from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import GroupSerializer, UserSerializer

# A ViewSet if a class that combines the logic for a set of related views.
# See t.ly/M109


# class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(APIView):
    """tbd"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, username=None):
        """Get a username.

        Try to get a username to see if it's already in use.
        """
        try:
            username = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'msg': 'name_not_in_use'})
            # Since username was not found, client *can* select this username.
            # return HttpResponse(status=404)
        return Response({'msg': 'name_in_use'})
        # Username was found so client *cannot* select this username.
        # return HttpResponse(status=200)
