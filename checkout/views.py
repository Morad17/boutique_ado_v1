from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hoy7pGfGpmHOSFZo7nDroHZe8OXb63QUy3P5Hhfa5kdYIZQdEwxfbeGSqgJoQ6cydL1By8EFbZtCwEu6gX7X1Oc00eFn0DirE',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)