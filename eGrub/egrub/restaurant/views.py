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

        # Loop through the order(s) and add the total price
        total_price = 0
        for order in orders:
            total_price += order.price

        # Pass the number of order(s) and total revenue into template
        context = {
            'orders': orders,
            'total_price': total_price,
            'total_orders': len(orders)
        }

        return render(request, 'restaurant/dashboard.html', context)

    def test_function(self):
        return self.request.user.groups.filter(name='Staff').exists()    