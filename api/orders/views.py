from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from api.pizzas.models import Pizza
from api.customers.models import Customer

@login_required
def customer_orders(request):
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(customer=customer)  # Fetch orders for the logged-in customer
    return render(request, 'order_templates/customer_orders.html', {'orders': orders})

@login_required
def place_order(request):
    pizzas = Pizza.objects.all()  # Display all available pizzas for ordering

    if request.method == 'POST':
        # Fetch the current customer
        customer = Customer.objects.get(user=request.user)

        # Create a new order
        order = Order.objects.create(customer=customer)
        total_price = 0

        # Loop through all pizzas and check if they were selected
        for pizza in pizzas:
            pizza_id = f'pizza_{pizza.id}'
            quantity_id = f'quantity_{pizza.id}'

            if pizza_id in request.POST:
                quantity = int(request.POST.get(quantity_id, 1))  # Get the quantity for the pizza
                OrderItem.objects.create(order=order, pizza=pizza, quantity=quantity)
                total_price += pizza.price * quantity

        # Update total price and save the order
        order.total_price = total_price
        order.save()

        # Redirect to 'customer_orders' to see order history
        return redirect('customer_orders')

    return render(request, 'order_templates/place_order.html', {'pizzas': pizzas})
