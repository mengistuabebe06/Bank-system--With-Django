from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from bankSystem.models import *
from bankSystem.serializers import *


class BranchsAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BankAPIView(generics.ListCreateAPIView):
    # give permmsiion
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BranchDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BankDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
