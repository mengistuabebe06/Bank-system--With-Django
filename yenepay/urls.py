from django.urls import path, include
from yenepay.views import payment, success, cancle

urlpatterns = [
    path("pay/", payment, name="pay"),
    path("success/", success, name="success"),
    path("cancle/", cancle, name="cancle"),
]
