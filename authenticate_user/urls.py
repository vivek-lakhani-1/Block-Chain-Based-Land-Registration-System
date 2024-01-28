
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register),
    path('/login',views.login_API_Web),
    path("/wallet_address",views.wallet_data),

    
]
