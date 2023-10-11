from django.shortcuts import render
from .models import Product

def product_list(request):
    # Retrieve data from the Product model
    products = Product.objects.all()
    product_list = []
    
    for product in products:
        # Access the JSON data from the 'data' field
        json_data = product.data
        
        # Extract specific values from the JSON data
        product_id = json_data.get('id')
        product_image = json_data.get('image')
        product_name = json_data.get('name')
        product_description = json_data.get('description')
        product_color = json_data.get('color')
        
        # Create a dictionary with the extracted values
        product_info = {
            'id': product_id,
            'image': product_image,
            'name': product_name,
            'description': product_description,
            'color': product_color,
        }
        
        # Append the product information to the list
        product_list.append(product_info)

    # Now you have a list of dictionaries, where each dictionary represents a product
    context = {'products': product_list}
    return render(request, 'cart/product_list.jinja2', context)
