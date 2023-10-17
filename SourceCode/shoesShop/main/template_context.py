from django.shortcuts import render
from .models import Banner,Category,Brand,Product,ProductAttribute
from django.db.models import Max,Min
def get_filters(request):
    cats = Product.objects.distinct().values('category__title','category__id')
    brands = Product.objects.distinct().values('brand__title','brand__id')
    colors = ProductAttribute.objects.distinct().values('color__title','color__id','color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title','size__id')
    minMaxPrice = ProductAttribute.objects.aggregate(Min('price'),Max('price'))
    data = {'cats':cats,'brands':brands,'colors':colors,'sizes':sizes,'minMaxPrice':minMaxPrice,}
    return data