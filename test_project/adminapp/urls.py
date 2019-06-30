from django.contrib import admin
from django.urls import path
import adminapp.views as adminapp
from django.conf import settings               # following 2 strings are added to spread media files
from django.conf.urls.static import static
from django.conf.urls import include

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.main, name='main'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.UserListView.as_view(), name='users'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.UserDeleteView.as_view(), name='user_delete'),
    #
    path('categories/update/', adminapp.CategoryCreateView.as_view(), name='category_update'),
    path('categories/read/', adminapp.CategoryListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.CategoryDeleteView.as_view(), name='category_delete'),
    #
    path('products/update/', adminapp.ProductCreateView.as_view(), name='product_update'),
    path('products/read/', adminapp.ProductListView.as_view(), name='products'),
    path('products/read/category/<int:pk>/', adminapp.ProductListView.as_view(), name='products_by_category'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]