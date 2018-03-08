from django.shortcuts import render
from django.contrib.auth.models import User, Group
from bidder.models import  Campaign, Keyword
from rest_framework import viewsets, generics
from bidder.serializers import UserSerializer, GroupSerializer, CampaignSerializer, KeywordSerializer


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
'''
class KeywordList(generics.ListAPIView):
    model = Keyword
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

class KeywordDetail(generics.RetrieveAPIView):
    model = Keyword
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    lookup_field = 'keyword'
'''
class KeywordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
'''
    def get_queryset(self):
        campaign = self.kwargs['campaign']
        return Keyword.objects.filter(pcampaign__directId=campaign)
'''      

class CampaignKeywordList(generics.ListAPIView):
    model = Keyword
    serializer_class = KeywordSerializer
    #queryset = Keyword.objects.filter(campaign__directId=self.kwargs.get('directId'))
    def get_queryset(self):
        #queryset = super(CampaignKeywordList, self).get_queryset()
        return Keyword.objects.filter(campaign__directId=self.kwargs.get('directId'))
