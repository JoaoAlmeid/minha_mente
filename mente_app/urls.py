from django.urls import path
from mente_app import views

urlpatterns = [
    path('', views.lista_itens, name='lista_itens'),
    path('criar_tarefa', views.create_item, name='create_item'),
    path('delete', views.delete_item, name="delete"),
    path('update_item', views.update_item, name="update_item"),
    path('update_status', views.update_status, name="update_status"),
]