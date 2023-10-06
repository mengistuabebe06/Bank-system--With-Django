from rest_framework import serializers
from bankSystem.models import (
    Bank,
    Branch,
    Client,
    ClientManager,
    Account,
    Deposite,
    Transfer,
    Withdraw,
)


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = Bank
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientManager
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    clients = ClientSerializer()
    bank = BankSerializer()

    class Meta:
        model = Account
        fields = "__all__"


class AccountDetailSerializer(serializers.ModelSerializer):
    clients = ClientSerializer()
    bank = BankSerializer()
    balance = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Account
        fields = ["clients", "bank", "balance", "open_date"]


class DepositeSerializer(serializers.ModelSerializer):
    # account = AccountSerializer()

    class Meta:
        model = Deposite
        fields = "__all__"


class TransferSerializer(serializers.ModelSerializer):
    # branch = BranchSerializer()
    # account = AccountSerializer()

    class Meta:
        model = Transfer
        fields = "__all__"


class WithdrawSerializer(serializers.ModelSerializer):
    # account = AccountSerializer()
    class Meta:
        model = Withdraw
        fields = "__all__"
