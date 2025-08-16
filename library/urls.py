from django.urls import path
from .views import BookListApiView, BookDetailApiView

urlpatterns = [
    path('kitoblar/', BookListApiView.as_view() ),
    path('kitob/<int:pk>/', BookDetailApiView.as_view() )
]
