from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Orders, Odetails, Parts, Customers


# Add home view function
def home_view(request):
    return render(request, "home.html")


def invoice_view(request):
    order_number = request.GET.get("order_number", None)

    if not order_number:
        # If no order_number was provided, redirect to the home page or show an error
        return redirect("home_view")

    # Fetch the order using the order_number, ensuring it exists
    order = get_object_or_404(Orders, ono=order_number)

    # Fetch related order details
    order_details = Odetails.objects.filter(ono=order_number).select_related("pno")
    # In case of multiple detail records, aggregate part information and calculate sums dynamically
    for detail in order_details:
        # Assuming detail.part is a Parts object fetched through a foreign key relation in Odetails
        detail.part_name = detail.pno.pname
        detail.part_price = detail.pno.prices
        detail.sum = detail.qty * detail.pno.prices

    # Calculate the total order sum
    total_sum = sum(detail.sum for detail in order_details)

    context = {
        "order": order,
        "customer": order.cno,  # Directly using the related Customer object
        "order_details": order_details,
        "total_sum": total_sum,
    }

    return render(request, "invoice.html", context)
