from django.urls import path
from .views import SnackListView,SnackDetailView
urlpatterns = [
    path('', SnackListView.as_view(),name='snack'), 
    path('detail/<pk>',SnackDetailView.as_view(),name='snack_details')
]