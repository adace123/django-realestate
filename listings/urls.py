from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListingIndexView.as_view(), name='listing_index'),
    path('<int:pk>/details/', views.ListingDetailsView.as_view(), name='listing_detail')
]