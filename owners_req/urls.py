from django.urls import path
from . import views
from django.conf.urls import url
from .views import CreateView, CreateCarView




app_name = 'owners_req'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', CreateView.as_view(), name='create'),
    path('createCar', CreateCarView.as_view(), name='createCar'),
    #path('PostCreate', PostCreate.as_view(), name='PostCreate'),
    path('edit', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('editCar/<int:num1>', views.editCar, name='editCar'),
    path('deleteCar/<int:num1>', views.deleteCar, name='deleteCar'),
    path('carlist', views.carlist, name='carlist'),
]
