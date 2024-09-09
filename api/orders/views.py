from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from api.pizzas.models import Pizza
from api.customers.models import Customer

@login_required
def customer_orders(request):
    customer = Customer.objects.get(user=request.user)
    orders = Order.objects.filter(customer=customer)  # Fetch orders for the logged-in customer
    return render(request, 'customer_orders.html', {'orders': orders})

@login_required
def place_order(request):
    pizzas = Pizza.objects.all()  # Display all available pizzas for ordering

    if request.method == 'POST':
        pizza_ids = request.POST.getlist('pizza')  # Get the selected pizza IDs
        quantities = request.POST.getlist('quantity')  # Get the quantities

        # Fetch the current customer
        customer = Customer.objects.get(user=request.user)

        # Create a new order
        order = Order.objects.create(customer=customer)
        total_price = 0

        # Loop through selected pizzas and create order items
        for pizza_id, quantity in zip(pizza_ids, quantities):
            pizza = Pizza.objects.get(id=pizza_id)
            quantity = int(quantity)
            OrderItem.objects.create(order=order, pizza=pizza, quantity=quantity)
            total_price += pizza.price * quantity

        # Update total price and save the order
        order.total_price = total_price
        order.save()

        # Redirect to 'customer_orders' to see order history
        return redirect('customer_orders')

    return render(request, 'place_order.html', {'pizzas': pizzas})



