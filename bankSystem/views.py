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


class AccountCreateAPIView(APIView):
    def post(self, request):
        try:
            # Extract data from request
            fullname = request.data.get("fullname")
            address = request.data.get("address")
            bank_id = request.data.get("bank")
            account_type = request.data.get("account_type")
            open_date = request.data.get("open_date")

            # Validate data
            if not all([fullname, address, bank_id, account_type, open_date]):
                return Response(
                    {"error": "Missing required field"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Create client
            client = Client.objects.create(
                name=fullname,
                address=address,
            )

            # Get bank
            try:
                bank = Bank.objects.get(pk=bank_id)
            except ObjectDoesNotExist:
                return Response(
                    {"error": "Bank not found"}, status=status.HTTP_404_NOT_FOUND
                )

            # Create account
            account = Account.objects.create(
                clients=client,
                bank=bank,
                account_type=account_type,
                open_date=open_date,
            )

            # Serialize and return data
            serializer = AccountSerializer(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
