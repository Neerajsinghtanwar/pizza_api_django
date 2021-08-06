from django.urls import path
from django.urls.conf import include
from  pizza_api import api_views, auth
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', api_views.UserView, basename='user')
router.register('staff', api_views.StaffView, basename='staff')
router.register('pizza', api_views.PizzaView, basename='pizza')
router.register('topping', api_views.ToppingView, basename='topping')
router.register('price', api_views.PriceView, basename='price')
router.register('order', api_views.OrderView, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', auth.AuthView.as_view({'post':'login', 'get':'loginview'}), name='loginauth'),
    path('logout/', auth.AuthView.as_view({'get':'logout'}), name='logoutauth'),
    path('usercsv/', api_views.ExportExcel.as_view()),
    path('auth/', include('rest_framework.urls', namespace='authentication'))
]