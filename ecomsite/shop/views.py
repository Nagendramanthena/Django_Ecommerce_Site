from .models import Products,Order
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    #Paginator
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    return render(request,'index.html',{'product_objects':product_objects})


def detail(request,id):
    product_objects = Products.objects.get(id = id)
    return render(request,'detail.html',{'product_object':product_objects})

def checkout(request):
    print(request.method)
    if request.method == "POST":
        print("YES");
        name = request.POST.get('name',"Nagendra")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        order = Order(name=name, email=email, address=address, city=city, state=state, zipcode=zipcode)
        order.save()
        print(name)
    return render(request,'checkout.html')

