from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        'name_project' : "Rich Shop",
        'npm' : '2406428806',
        'name': 'Auriel Erich Ibrahim Nst',
        'class': 'PBP F',
        'products': products,
    }
    return render(request, "main.html", context)