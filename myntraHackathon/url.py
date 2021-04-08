from django.urls import path

from . import views1

urlpatterns = [

    
    path('',views1.open),
    path('draw',views1.draw),
    path('up', views1.simple_upload, name = 'create'),
    path('results',views1.check_results),
    path('products',views1.view_products),
]