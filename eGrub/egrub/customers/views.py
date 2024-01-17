from django.shortcuts import render
from django.views import View
from .models import MenuItems, Category, OrderModel 

class IndexPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customers/index.html')


class AboutPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customers/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # Retrieve each item from each category
        appetisers = MenuItems.objects.filter(category__name__contains='Appetiser')
        entres = MenuItems.objects.filter(category__name__contains='Entre')
        drinks = MenuItems.objects.filter(category__name__contains='Drink')
        sauces = MenuItems.objects.filter(category__name__contains='Sauce')

        # Pass into context
        context = {
            'appetisers': appetisers,
            'entres': entres,
            'drinks': drinks,
            'sauces': sauces,
        }

        return render(request, 'customers/order.html', context)

    # Define the 'POST' method for orders
    def post(self, request, *args, **kwargs):
        # Grab all selected items, get menu item, return name, price and id to calculate total order price
        order_items = {
            'items': []
        }

        # Retrieve all items, set the name of every input to 'items[]'
        items = request.POST.getlist('items[]')

        # Loop through all items and grab all the data required
        for item in items:
            menu_item = MenuItems.objects.get(pk=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            # Append item data into the items list within the items dictionary
            order_items['items'].append(item_data)

            # Calculate the total order price 
            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        # Create order oject and append all menu items
        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)

        # Pass into context
        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'customers/order_confirm.html', context)     