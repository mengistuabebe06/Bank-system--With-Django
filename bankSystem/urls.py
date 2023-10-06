from django.urls import path, include
from bankSystem.views import (
    BankAPIView,
    BranchsAPIView,
    BranchDetailsAPIView,
    BankDetailsAPIView,
)

urlpatterns = [
    path("branchs/", BranchsAPIView.as_view(), name="branchs"),
    path("banks/", BankAPIView.as_view(), name="banks"),
    path("branchs/<int:pk>/", BranchDetailsAPIView.as_view(), name="branchsdetails"),
    path("banks/<int:pk>/", BankDetailsAPIView.as_view(), name="bankdetails"),
]
