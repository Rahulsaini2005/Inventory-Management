from django.urls import path, include

from apps.product import views
from apps.product.views import CreateProduct, ListProductView, ListProductViewJson, ProductUpdateView, \
    ProductDeleteView, ProductDetailView

urlpatterns = [
    path('product_rest_api/',include('apps.product.product_rest_api.urls')),
    path('product',views.product,name='new-product'),
    path('admin/product',CreateProduct.as_view(),name='add-product'),
    path('admin/product/list',ListProductView.as_view(),name='add-product-list'),
    path('admin/product/list/ajax', ListProductViewJson.as_view(), name='admin-product-list-ajax'),
    path('UpdateView/<int:pk>/',ProductUpdateView.as_view(),name='admin-product-edit'),
    path('DeleteView/<int:pk>/',ProductDeleteView.as_view(), name='admin-product-delete'),
    path('admin/detail<int:pk>/',ProductDetailView.as_view(),name='admin-product-detail')
    # path('save/<int:product_id>/images/', manage_product_images, name='manage_product_images')
]
