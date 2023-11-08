from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, index
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='menu_items'),
    path('menu/<int:pk>', SingleMenuItemView.as_view(), name='menu_item'),
    path('api-token-auth/', obtain_auth_token),
]