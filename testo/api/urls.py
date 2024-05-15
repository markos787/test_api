from django.urls import path
from . import views

urlpatterns=[
    path('zasadzki/', views.zasadzkiView.as_view(), name='zasadzki-list'),
    path('zasadzki/s', views.zasadzkiSearchView.as_view(), name='zasadzki-list-create'),
    path('zasadzki/t', views.zasadzki_table, name='zasadzki-table'),
    path('zasadzki/<int:pk>/', views.zasadzkiRetrieveUpdateDestroy.as_view(), name='zasadzki-detail'),

]
