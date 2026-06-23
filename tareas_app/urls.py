from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'tareas'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.TareaListView.as_view(), name='tarea_list'),
    path('crear/', views.TareaCreateView.as_view(), name='tarea_create'),
    path('editar/<int:pk>/', views.TareaUpdateView.as_view(), name='tarea_edit'),
    path('eliminar/<int:pk>/', views.TareaDeleteView.as_view(), name='tarea_delete'),
]

