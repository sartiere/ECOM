from django.shortcuts import render
from .models import Product, Commande
from django.core.paginator import Paginator
from django.shortcuts import redirect

# Create your views here.
def index(request):
    Product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        Product_object = Product.objects.filter(title__icontains=item_name)
    paginator = Paginator(Product_object, 4)
    page = request.GET.get('page')
    Product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'Product_object': Product_object})

def detail(request, myid):
    Product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': Product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        
        com = Commande(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays)
        com.save()
        return redirect('confirmation')

    return render(request, 'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    
    return render(request, 'shop/confirmation.html', {'name':nom})


def product_list(request):
    products = Product.objects.all()  # Récupère tous les produits depuis la base de données
    return render(request, 'shop/liste_pro.html', {'products': products})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})
