from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe

# Create your views here.
def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "No Items found in your basket, please add items to proceed to checkout.")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51Q8k2hERTQF2ci7FVdDSNnLRvnFJkEMisl4XrEaxJa6322sKSsctKgR1D7vaVpBb90kMQdyyeRdvThHRR6hgESP700CsvNMqL2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)