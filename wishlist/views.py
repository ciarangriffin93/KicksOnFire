from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist, Product  # Adjust according to your actual models
from django.contrib.auth.decorators import login_required


@login_required
def wishlist(request):
    # Fetch the user's wishlist items
    user_wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'user_wishlist': user_wishlist})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Check if the product is already in the user's wishlist
    if not Wishlist.objects.filter(user=request.user, product=product).exists():
        Wishlist.objects.create(user=request.user, product=product)
    return redirect('wishlist')  # Redirect back to the wishlist

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Remove the product from the user's wishlist
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first()
    if wishlist_item:
        wishlist_item.delete()
    return redirect('wishlist')  # Redirect back to the wishlist