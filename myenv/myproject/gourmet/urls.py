from django.urls import path
from . import views

app_name = 'gourmet'
urlpatterns = [
    path('',views.TopView.as_view(), name='top'),
    path('detail/<int:pk>',views.StoreDetailView.as_view(),name='detail'),
    path('profile/',views.ProFileView.as_view(),name='profile'),
]