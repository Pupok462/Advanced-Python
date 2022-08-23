from django.urls import path
from .views import (
    DevicesListView,
    DevicesTypeListView,
    DevicesDetailView,
    DeviceDeleteView,
    DeviceCreateView,
    SliderListView,
)
app_name = 'devices'

urlpatterns = [
    path('', SliderListView.as_view(), name='slider'),
    path('product_list/', DevicesListView.as_view(), name='devices-list'),
    path('create/', DeviceCreateView.as_view(), name='create'),
    path('<int:pk>/', DevicesDetailView.as_view(), name='details'),
    path('<str:type_name>/', DevicesTypeListView.as_view(), name='type-list'),
    path('<int:pk>/delete/', DeviceDeleteView.as_view(), name='delete'),
]



