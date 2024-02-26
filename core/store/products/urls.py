from django.urls import path
from .views      import ProductsView

urlpatterns = [
    path('',               ProductsView.as_view(), name='products'),
    path('<int:item_id>/', ProductsView.as_view(), name='product-detail'),
]
