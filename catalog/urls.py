from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.YachtListView.as_view(), name='shop'),
    path('yacht/<int:pk>', views.YachtDetailView.as_view(), name='yacht-detail')
]
