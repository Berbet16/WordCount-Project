
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='home'),
    path('count/', views.count, name='count'), #urladı, fonksiyonu çağırma
    path('about/', views.about, name='about')
]
