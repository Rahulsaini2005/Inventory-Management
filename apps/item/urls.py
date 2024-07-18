from django.urls import path, include

from apps.item import views
from apps.item.views import CreateItem, ListItemView,ListItemViewJson

urlpatterns = [
    path('item_rest_api/',include('apps.item.item_rest_api.urls')),
    path('item',views.mukesh),
    path('admin/item',CreateItem.as_view(),name='item'),
    path('admin/Item', ListItemView.as_view(), name='admin-item-list'),
    path('admin/Item/list/ajax', ListItemViewJson.as_view(), name='admin-item-list-ajax'),
    path('upload/', views.upload_csv, name='upload-csv'),
]