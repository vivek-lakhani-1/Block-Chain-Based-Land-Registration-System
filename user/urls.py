
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard),
    path('/add-land', views.add_data_land),
    path('/all-land', views.all_land_data),
    path('/review', views.review),
    path('/wallet', views.wallet),

    
]
