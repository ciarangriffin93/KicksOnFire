from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist, Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def wishlist(request):
    user_wishlist = Wishlist.objects.filter(user=request.user)
    return render(
        request, 'wishlist/wishlist.html', {'user_wishlist': user_wishlist})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not Wishlist.objects.filter(user=request.user, product=product).exists(): # noqa
        Wishlist.objects.create(user=request.user, product=product)
        messages.success(request,
                         f'{product.name} has been added to your wishlist.')
    else:
        messages.info(request, f'{product.name} is already in your wishlist.')

    next_url = request.GET.get('next', 'wishlist')
    return redirect(next_url)


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first() # noqa
    if wishlist_item:
        wishlist_item.delete()
        messages.success(
            request, f'{product.name} has been removed from your wishlist.')
    else:
        messages.info(request, f'{product.name} was not in your wishlist.')

    next_url = request.GET.get('next', 'wishlist')
    return redirect(next_url)
