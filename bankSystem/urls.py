from django.urls import path, include
from bankSystem.views import (
    BankAPIView,
    BranchsAPIView,
    BranchDetailsAPIView,
    BankDetailsAPIView,
    AccountCreateAPIView,
    AccountListAPIView,
    DepositeAPIView,
    WithDrawAPIView,
    AccountDetailAPIView,
)

urlpatterns = [
    path("branchs/", BranchsAPIView.as_view(), name="branchs"),
    path("banks/", BankAPIView.as_view(), name="banks"),
    path("branchs/<int:pk>/", BranchDetailsAPIView.as_view(), name="branchsdetails"),
    path("banks/<int:pk>/", BankDetailsAPIView.as_view(), name="bankdetails"),
    path("create_account/", AccountCreateAPIView.as_view(), name="create_account"),
    path("accounts/", AccountListAPIView.as_view(), name="accounts"),
    path("deposite/", DepositeAPIView.as_view(), name="deposite"),
    path("withdraw/", WithDrawAPIView.as_view(), name="withdraw"),
    path("accounts/<int:pk>/", AccountDetailAPIView.as_view(), name="account_detail"),
]
