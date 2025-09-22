# puddle/item/urls.py

from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    # ... other URL patterns
    path('', views.items, name='items'), # This line was the error
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('new/', views.new, name='new'),
]