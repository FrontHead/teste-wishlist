from django.db import models
from djongo import models
from concurrent.futures import ThreadPoolExecutor
import time
import requests
import asyncio

class Client(models.Model):
    id_client = models.UUIDField(default=False)
    nome = models.CharField(db_column='nome', max_length=100, blank=False)
    email = models.TextField(db_column='email', max_length=100, blank=False)
    wishlist = models.JSONField(db_column='wishlist', max_length=1000, blank=True)

# class Wishlist(models.Model):
#     id_wishlist = models.ObjectIdField(default=True)
#     cliente = models.ForeignKey(Client,on_delete=models.CASCADE, unique=False)
#     product_id = models.JSONField()

#     #update your model
#     def serialize(self):
#         return{
#            "cliente": self.cliente.id,
#            "product_id": self.product_id
#         }
#     def __str__(self):
#         return str(self.product_id)

#     def updateList(self, id_produto):
#         produtos_dict = json.loads(product_id)
#         product_id.update(produtos_dict)
#         print(product_id)

#         return pro
        
class ProductRequest:

    def __init__(self, request, page, r=f'http://challenge-api.luizalabs.com/api/product/?page='):
        self.request = request
        self.page = page        
        self.r = r

    def getProducts(self):

        return requests.get(self.r+f"{self.page}").json()

    def request_pageSize(self):
        
        return requests.get(self.r+f"{self.page}").json()['meta']['page_size']

    async def request_runner():
        # Controle de thread
        _executor = ThreadPoolExecutor(2)
        await loop.run_in_executor(_executor, __init__(1))