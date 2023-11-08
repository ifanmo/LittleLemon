from django.urls import path
from .views import MenuItemsView, SingleMenuItemView, BookingsView, SingleBookingView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', MenuItemsView.as_view(), name='menu_items'),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view(), name='menu_item'),
    path('bookings/', BookingsView.as_view(), name='menu_items'),
    path('bookings/<int:pk>', SingleBookingView.as_view(), name='menu_item'),
    path('api-token-auth/', obtain_auth_token),
]