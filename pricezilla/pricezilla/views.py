from django.shortcuts import render
from product.models import Product

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request,"about.html")
 
def wishlist(request):
    return render(request, 'wishlist.html')

def howreviews(request):
    return render(request, 'how-we-show-reviews.html')

def registershop(request):
    return render(request, 'register-shop.html')

def rulesandguide(request):
    return render(request, 'rules-and-guidelines.html')

def contactpricezilla(request):
    return render(request, 'contact-pricezilla.html')
    
def signup(request):
    return render(request, 'sign-up.html')


def contact(request):
    return render(request, "contact.html")

def account(request):
    return render(request, "account-info.html")

def profile(request):
    return render(request, "profile.html")

def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if not query:
            return HTTPResponse("Search bar is empty")
        if Product.objects.filter(name__icontains=query).exists():
            products = Product.objects.filter(name__icontains=query) 
            return render(request, 'search.html', {'products':products})
        else:
            print("No product found")
            return render(request, 'search.html', {})
      
