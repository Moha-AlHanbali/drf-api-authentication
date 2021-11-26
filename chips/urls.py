from django.urls import path
from .views import ChipsListView, ChipsDetailView

urlpatterns = [
    path('', ChipsListView.as_view(), name='chips-list'),
    path('<int:pk>/', ChipsDetailView.as_view(), name='chips-detail'),
]