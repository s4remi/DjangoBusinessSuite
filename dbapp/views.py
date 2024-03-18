from django.shortcuts import render, redirect

# Create your views here.
from .models import Orders, Odetails, Parts, Customers


# Add home view function
def home_view(request):
    return render(request, "home.html")


def invoice_view(request, order_number):
    # Get the order based on the order_number
    try:
        order = Orders.objects.get(ono=order_number)
    except Orders.DoesNotExist:
        return render(request, "order_not_found.html", {"order_number": order_number})

    # Fetch related details
    order_details = Odetails.objects.filter(ono=order_number)
    customer = Customers.objects.get(cno=order.cno)

    # Enhance order_details with part information
    for detail in order_details:
        detail.part = Parts.objects.get(pno=detail.pno)
        detail.sum = detail.qty * detail.part.prices

    # Calculate the total order sum
    total_sum = sum(detail.sum for detail in order_details)

    context = {
        "order": order,
        "customer": customer,
        "order_details": order_details,
        "total_sum": total_sum,
    }

    return render(request, "invoice.html", context)
