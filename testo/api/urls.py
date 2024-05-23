from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns=[
    path('', views.main_view, name='main-view'),
    path('zasadzki/', views.zasadzkiView.as_view(), name='zasadzki-list'),
    path('zasadzki/s', views.zasadzkiSearchView.as_view(), name='zasadzki-list-create'),
    path('zasadzki/t', views.zasadzki_table, name='zasadzki-table'),
    path('zasadzki/m', views.LocationView.as_view(), name='zasadzki-map'),
]
