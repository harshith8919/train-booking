from django.urls import path
from . import views

urlpatterns = [
    path('', views.train_list, name='train-list'),
    path('<int:pk>/book/', views.book_seat, name='book-seat'),
]
