from django.shortcuts import render
from arkapp.models import Product
from math import ceil
# Create your views here.
def home(request):
    current_user = request.user
    print(current_user)
    allProds = []
    catProds = Product.objects.values('category','id')
    cats ={item['category']for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n /4) - (n//4))
        allProds.append([prod,range(1, nSlides), nSlides])
    params= {'allProds':allProds}    
    return render(request, 'index.html',params)
