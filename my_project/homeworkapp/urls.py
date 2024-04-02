from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('create_users_fake/', views.create_users_fake, name='create_users_fake'),
    # path('create_products/', views.create_products, name='create_products'),

]
