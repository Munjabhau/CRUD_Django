from django.urls import path
from . import views

urlpatterns = [
    path('', views.retrieve, name="retrieve"),
    path('index', views.index, name="index"),
    path('create', views.create, name="create"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delet/<int:id>', views.delet, name="delet"),
]
