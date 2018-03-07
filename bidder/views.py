from django.shortcuts import render
from django.contrib.auth.models import User, Group
from bidder.models import  Campaign
from rest_framework import viewsets
from bidder.serializers import UserSerializer, GroupSerializer, CampaignSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer