from django.urls import path
from .views import *

urlpatterns = [    
    path('', BookListView.as_view(), name='book-list'),
    path('book-detail/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('book-update/<int:pk>/', BookUpdate.as_view(), name='book-update'),
    path('book-create/', BookCreate.as_view(), name='book-create'),
    path('book-delete/<int:pk>/', BookDelete.as_view(), name='book-delete'),

    
]