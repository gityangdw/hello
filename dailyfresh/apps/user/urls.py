from django.conf.urls import url
from .views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView
urlpatterns = [
    # url(r'^register$', views.register, name='regiser'),
    # url(r'^register_handle$', views.register_handle, name='regiser_handle'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),


    url(r'^$', UserInfoView.as_view(), name='user'),
    url(r'^address/', AddressView.as_view(), name='address'),
    url(r'^order/(?P<page>\d+)$', UserOrderView.as_view(), name='order'),
]
