"""wishlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
# from .models import Wishlist
from django.urls import path

urlpatterns = [    
    path('produtos/<str:page>', views.productPage, name='produtos'),
    path('produtos/adicionar', views.updateWishlist),
    # path('adicionar', views.updateWishlist, name='wishlist'),
    path('client-list', views.clientList, name='client-list'),
    path('client-create', views.clientCreate, name='client-create'),
    path('client-update/<int:id>', views.clientUpdate, name='client-update'),
    path('client-delete/<int:id>', views.clientDelete, name='client-delete'),
]
