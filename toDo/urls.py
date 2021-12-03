from django.urls import path

from toDo import views

app_name = 'toDo'

urlpatterns = [
    path('', views.toDo_list, name='toDo_list'),
    path('create/', views.toDo_create, name='toDo_create'),
    path('<int:pk>/delete/', views.toDo_delete, name='toDo_delete'),
    
    path('<int:pk>/toDo/complete/', views.toDo_complete, name='toDo_complete'),
    path('<int:pk>/toDo/incomplete/', views.toDo_incomplete, name='toDo_incomplete'),

    path('<int:pk>/', views.toDo_detail, name='toDo_detail'),
    path('<int:pk>/update/', views.toDo_update, name='toDo_update'),
]
