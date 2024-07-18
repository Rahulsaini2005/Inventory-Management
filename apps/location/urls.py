from django.urls import path

from apps.location import views
from apps.location.views import ListLocationView, ListLocationViewJson, StoreCreateView, \
    ListCustomerLocationView, ListLocationDetailViewJson, AreaTemplateView, AreaCreateView, ListLocationAreaViewJson, \
    AsileTemplateView, AisleCreateView, ListLocationAisleViewJson, UprightTemplateView, UprightCreateView, \
    ListLocationUprightViewJson, AssignItemTemplateView, AssignItemCreateView,ListLocationAssignItemViewJson

urlpatterns = [
    path('location',views.location),
    path('store/add/<int:customer_id>/', StoreCreateView.as_view(), name='store-add'),
    path('admin/location/', ListLocationView.as_view(), name='admin-location-list'),
    path('admin/location/list/ajax', ListLocationViewJson.as_view(), name='admin-Location-list-ajax'),
    path('admin/location/detail/list/ajax/<int:customer_id>/', ListLocationDetailViewJson.as_view(), name='admin-Location-detail-list-ajax'),
    path('admin/location/detail/<int:customer_id>', ListCustomerLocationView.as_view(), name='admin-location-detail'),


    path('admin/location/area/<int:store_id>/', AreaTemplateView.as_view(), name='admin-location-area'),
    path('area/add/<int:store_id>/', AreaCreateView.as_view(), name='area-add'),
    path('admin/location/area/ajax/<int:store_id>/', ListLocationAreaViewJson.as_view(), name='admin-Location-area-ajax'),

    # aisle path
    path('admin/location/asile/<int:area_id>', AsileTemplateView.as_view(), name='admin-location-asile'),
    path('aisle/add/<int:area_id>', AisleCreateView.as_view(), name='aisle-add'),
    path('admin/location/aisle/ajax/<int:area_id>', ListLocationAisleViewJson.as_view(), name='admin-Location-aisle-ajax'),

    # upright path
    path('admin/location/upright/<int:aisle_id>', UprightTemplateView.as_view(), name='admin-location-upright'),
    path('upright/add/<int:aisle_id>', UprightCreateView.as_view(), name='upright-add'),
    path('admin/location/upright/ajax/<int:aisle_id>', ListLocationUprightViewJson.as_view(), name='admin-Location-upright-ajax'),

    # assign item
    path('admin/location/assign/<int:upright_id>', AssignItemTemplateView.as_view(), name='admin-location-assign'),
    path('assign/add/<int:upright_id>', AssignItemCreateView.as_view(), name='assign-add'),
    path('admin/location/assign/ajax/<int:upright_id>', ListLocationAssignItemViewJson.as_view(), name='admin-Location-assign-ajax'),
]