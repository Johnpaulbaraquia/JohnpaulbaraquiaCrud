from django.urls import path
from .views import HomepageView, AboutpageView, ContactpageView
from .views import(
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,)

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('contact/', ContactpageView.as_view(), name='contact'),
    
    path('order/', OrderListView.as_view(), name='order'),    
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('order/', OrderListView.as_view(), name='order_list'),
    # path('order/success/', TemplateView.as_view(template_name='app/order_success.html'), name='order_success'),
]