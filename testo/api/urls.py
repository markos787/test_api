from django.urls import path
from . import views

urlpatterns=[
    path('zasadzki/', views.zasadzkiList.as_view(), name='zasadzki-list'),
    path('zasadzki/s', views.zasadzkiSearchView.as_view(), name='zasadzki-list-create'),
    path('zasadzki/t', views.zasadzkiList.zasadzki_table, name='zasadzki-table'),
    path('zasadzki/<int:pk>/', views.zasadzkiRetrieveUpdateDestroy.as_view(), name='zasadzki-detail'),
]
