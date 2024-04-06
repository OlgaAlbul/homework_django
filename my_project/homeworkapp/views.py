from random import choice

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
import logging
from .models import Clients, Products, Orders

logger = logging.getLogger(__name__)


def main(request):
    context = {
        'title': 'Главная',
        'message': 'Приветствуем вас на странице нашего магазина!'
    }
    logger.info("Главная страница загружена успешно")
    return render(request, 'homeworkapp/main.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'message': 'На этой странице вы можете узнать нас немного лучше'
    }
    logger.info("Страница 'О нас' загружена успешно")
    return render(request, 'homeworkapp/about.html', context)


def clientorders(request, cl_id):
    client = get_object_or_404(Clients, id=cl_id)
    # client = Clients.objects.filter(pk=cl_id)
    ord = {}
    # orders = Orders.objects.prefetch_related('products').select_related('order_prods').filter(customer_id=cl_id)
    for order in Orders.objects.all():
        if order.customer == client:
            ord[order.id] = order.date_ordered

    context = {'title': 'Заказы',
               'client': client.name,
               'orders': ord
               }
    return render(request, 'homeworkapp/clientorders.html', context)

# def create_users_fake(request):
#     for i in range(1, 10):
#         client = Clients(name=f'Name{i}', email=f'name{i}@mail.ru',
#                          phone=f'{11111111111}*{i}', address=f'Street{i}, home {i*2}')
#         client.save()
#         for j in range(1, 5):
#             ts = 0
#             prod = Products.objects.filter(pk=j).first()
#             ts += prod.price
#             order = Orders(customer=client, total_price=ts)
#             order.save()
#             order.products.add(prod)
#             order.save()
#
#     return HttpResponse('Ok')

# def create_products(request):
#     for i in range(1, 5):
#         product = Products(title=f'Title{i}', description=f'Description {i}',
#                            price=i*1000, count=i)
#         product.save()
#     return HttpResponse('Ok')
