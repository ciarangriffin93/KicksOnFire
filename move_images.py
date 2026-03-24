import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kicksonfire.settings")
django.setup()

from products.models import Product
import cloudinary.uploader

for product in Product.objects.all():
    if product.image:
        try:
            local_path = product.image.path

            if os.path.exists(local_path):
                print(f"Uploading {local_path}...")

                result = cloudinary.uploader.upload(local_path)

                # Save Cloudinary public_id
                product.image = result['public_id']
                product.save()

                print(f"Uploaded: {result['secure_url']}")

        except Exception as e:
            print(f"Error with {product.name}: {e}")