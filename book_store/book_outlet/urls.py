from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:book_slug>/', views.book_detail, name='book-detail'),

]
