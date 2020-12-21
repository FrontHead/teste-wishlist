from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from .models import Client, ProductRequest
from .forms import ClientForm

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def clientList(request):  
    clients = Client.objects.all()  
    return render(request,"client-list.html",{'clients':clients})  

def clientCreate(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('client-list')
            except:
                pass
    else:
        form = ClientForm()
    return render(request,'client-create.html',{'form':form})  

def clientUpdate(request, id):  
    client = Client.objects.get(id=id)
    form = ClientForm(initial={'nome': client.nome, 'e-mail': client.email})
    if request.method == "POST":  
        form = ClientForm(request.POST, instance=client)  
        if form.is_valid():  
            try:
                form.save()
                model = form.instance
                return redirect('/client-list')
            except Exception as e:
                pass
    return render(request,'client-update.html',{'form':form})

def clientDelete(request, id):
    client = Client.objects.get(id=id)
    try:
        client.delete()
    except:
        pass
    return redirect('client-list')

@transaction.atomic
def updateWishlist(request, id, prd_id):

    print(prd_id)

    client_wishlist = Client.objects.get(id=id).wishlist
    # form = wishlistForm(initial={'cliente': wishlist.nome, 'e-mail': wishlist.email})
    if request.method == "POST":  
        client_wishlist.asset.append(prd_id)
        client_wishlist.save()

@csrf_exempt
def productPage(request, page):
    # client = Client.objects.get(id=id)

    if request.method == "GET":

        produtos = ProductRequest('GET', page).getProducts()
        produtos_dict = produtos["products"]
        context = {
            'produtos': produtos_dict
            # '_produtos_':  "TETE"
        }
        # print(produtos_dict)
        # print( render(request, 'produtos.html', context, status=200) )
        return render(request, 'produtos.html', context, status=200)
    
    

    
    