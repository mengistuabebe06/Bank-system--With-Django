from django.shortcuts import render


def payment(request):
    obj = {
        "Process": "Express",
        "successUrl": "http://localhost:8000/success",
        "ipnUrl": "http://localhost:8000/ipn",
        "cancelUrl": "http://localhost:8000/cancel",
        "ItemName": "mango",
        "ItemId": 1,
        "UnitPrice": 15,
        "Quantity": 1,
        "ExpiresAfter": 12,
        "DeliveryFee": 0.0,
        "HandlingFee": 0.0,
        "Tax1": 0.0,
        "Tax2": 0.0,
        "Discount": 0.0,
        "MerchantId": "31119",
        # MerchantId=31119"
        # MerchantId=31119"
        # "totalItemsDeliveryFee": 19,
        # "totalItemsDiscount": 1,
        # "totalItemsHandlingFee": 12,
        # "totalItemsTax1": 250,
        # "totalItemsTax2": 0,
    }
    return render(request, "yenepay/index.html", {"obj": obj})


def success(request):
    return render(request, "yenepay/success.html")


def cancle(request):
    return render(request, "yenepay/cancle.html")
