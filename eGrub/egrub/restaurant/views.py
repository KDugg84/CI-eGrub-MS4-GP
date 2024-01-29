from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customers.models import OrderModel


# Define class to render the staff dashboard to view customer orders
class StaffDashboard(View, LoginRequiredMixin, UserPassesTestMixin):
    def get(self, request, *args, **kwargs):
        # Get the current date of the order
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, 
            created_on__day=today.day)

        # Loop through the order(s) and add the total price, check if order has not been dispatched
        undispatched_orders = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

            if not order.has_shipped:
                undispatched_orders.append(order)

        # Pass the number of order(s) and total revenue into template
        context = {
            'orders': undispatched_orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, 'restaurant/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()

# Define class to render template to view order details
class OrderInformation(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        # Get the order details from the current order
        order = OrderModel.objects.get(pk=pk)

        # Pass into context
        context = {
            'order': order
        }

        return render(request, 'restaurant/order_information.html', context)

    # POST method to send order_information form to the database     
    def post(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order.has_shipped = True
        order.save()

        # Pass into context
        context = {
            'order': order
        }

        return render(request, 'restaurant/order_information.html', context)   

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()