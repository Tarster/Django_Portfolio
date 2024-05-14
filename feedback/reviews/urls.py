from django.urls import path
from . import views
urlpatterns = [
    path('', views.ReviewView.as_view(), name='index'),
    path('thank-you/', views.ThankYouView.as_view(), name='thank_you'),
    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', views.SingleReviewView.as_view(), name='review'),
]
