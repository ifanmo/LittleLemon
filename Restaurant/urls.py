from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, index

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='menu_items'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu_item'),
    
]