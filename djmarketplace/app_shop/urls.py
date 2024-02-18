from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import register_view, CustomLoginView, CustomLogoutView, MainView, UserUpdateView, CarttView, \
    add_good_to_cart, pay

#new
from .views import BalanceRechargeView
from .views import delete_from_cart



urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('', MainView.as_view(), name='main'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
    path('balance_recharge/', BalanceRechargeView.as_view(), name='balance_recharge'),
    path('cart/', CarttView.as_view(), name='cart'),
    path('add_good/<int:pk>/', add_good_to_cart, name='add_good'),
    path('delete-from-cart/<int:item_id>/', delete_from_cart, name='delete_from_cart'),
    path('cart/pay/<int:pk>/', pay, name='pay'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)