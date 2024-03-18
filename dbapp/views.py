from django.shortcuts import render, redirect

# Create your views here.
from .models import Orders, Odetails, Parts, Customers


# Add home view function
def home_view(request):
    return render(request, "home.html")


def invoice_view(request, order_number):
    order_number = request.GET.get("order_number")

    if not order_number:
        # Redirect back to home if no order_number is provided
        return redirect("home_view")
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
