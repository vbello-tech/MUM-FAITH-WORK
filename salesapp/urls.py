from django.urls import path
from. import views

urlpatterns = [
    path('product/', views.product_list, name="product_list"),
    path('product/<int:pk>/', views.product_content, name="product_content"),
    path('product/add_post/', views.add_product, name="add_product"),
    path('product/<int:pk>/edit/', views.product_content_edit, name="product_content_edit"),
    path('product/<int:pk>/comment/', views.add_productcomments, name="add_productcomments"),
]