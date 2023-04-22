from django.urls import path, include
from . import views
import debug_toolbar

urlpatterns = [
    path('', views.index, name='index'),
    path('yachts/', views.YachtListView.as_view(), name='shop'),
    path('yachts/<int:pk>', views.YachtDetailView.as_view(), name='yacht-detail'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('cart/<int:pk>', views.CartDetailView.as_view(), name='cart'),
]
