from rest_framework import serializers
from bankSystem.models import Bank, Branch, Client, ClientManager


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    # branch = BranchSerializer()

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
