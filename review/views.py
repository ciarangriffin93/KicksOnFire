from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import ReviewForm

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()  # Fetch all reviews related to the product
    review_form = ReviewForm()

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = Review(
                product=product,
                user=request.user,  # Assign the current user
                title=review_form.cleaned_data['title'],
                rating=review_form.cleaned_data['rating'],
                text=review_form.cleaned_data['text']
            )
            review.save()  # Save the review to the database
            return redirect('product_detail', product_id=product.id)

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, 'products/product_detail.html', context)