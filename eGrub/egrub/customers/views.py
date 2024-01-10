from django.shortcuts import render
from django.views import View 

class index_page(View):
    def get(self, request, *args, **kwargs ):
        return render(request, 'customers/index.html')


class about_page(View):
    def get(self, request, *args, **kwargs ):
        return render(request, 'customers/about.html')