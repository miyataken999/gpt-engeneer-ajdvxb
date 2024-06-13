from django.shortcuts import render
from .models import Shop
from django.db.models import Q

def search(request):
    query = request.GET.get('q')
    shops = Shop.objects.filter(
        Q(category__icontains=query) |
        Q(subcategory__icontains=query) |
        Q(name__icontains=query)
    ).filter(price__gte=0, price__lte=4.41)
    return render(request, 'shop/index.html', {'shops': shops})