from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:book_id>/', views.book_detail, name='book-detail'),

]
