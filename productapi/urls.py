from  django.urls import path
from  .views import ProductUpdateApiView , ProductListApiView, ProductMixedApiView, ProductCreateApiView, ProductDeleteApiView, ProductDetailApiView



urlpatterns = [
    path('products/', ProductListApiView.as_view() ),
    path('product/<int:pk>/detail', ProductDetailApiView.as_view() ),
    path('product/<int:pk>/delete', ProductDeleteApiView.as_view() ),
    path('product/<int:pk>/update', ProductUpdateApiView.as_view() ),
    path('product/<int:pk>/mixed', ProductMixedApiView.as_view() ),
    path('product/create/', ProductCreateApiView.as_view() ),

]