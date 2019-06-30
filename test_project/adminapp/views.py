from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

# Create your views here.


class IsSuperUserView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class ProductListView(IsSuperUserView, ListView):
    model = Product
    template_name = 'adminapp/products.html'
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        if 'pk' in self.kwargs:
            if self.kwargs['pk']:
                queryset = queryset.filter(category=self.kwargs['pk'])
        return queryset

# тут переопределили стандаптный метод класса ListView, вписав в него новые ключевые слова.
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Все продукты.'
        context['categories'] = ProductCategory.objects.all()
        return context


class ProductDetailView(IsSuperUserView, DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    def get_queryset(self):
        queryset = super(ProductDetailView, self).get_queryset()
        if 'pk' in self.kwargs:
            if self.kwargs['pk']:
                queryset = queryset.filter(pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Продукт.'
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Новый продукт.'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin_custom:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        object_name = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Админка. Удаление продукта {}.'.format(object_name)
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:products')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        object_name = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Админка. Редактирование {}.'.format(object_name)
        return context

    def get_success_url(self):
        return reverse_lazy('admin_custom:product_read', kwargs={'pk': self.kwargs.get('pk')})


class CategoryListView(IsSuperUserView, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    queryset = ProductCategory.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Все категории.'
        return context


class CategoryCreateView(IsSuperUserView, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Новая категория.'
        return context


class CategoryDeleteView(DeleteView, IsSuperUserView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin_custom:categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        cat_name = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Админка. Удалить Категорию {}.'.format(cat_name)
        return context


class CategoryUpdateView(UpdateView, IsSuperUserView):
    model = ProductCategory
    template_name = 'adminapp/category.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        cat_name = ProductCategory.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Админка. Редактируем категорию {}.'.format(cat_name)
        return context


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    queryset = ShopUser.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        return context


class UserCreateView(CreateView, IsSuperUserView):
    model = ShopUser
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:users')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Новый Пользователь.'
        return context


class UserDeleteView(DeleteView, IsSuperUserView):
    model = ShopUser
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin_custom:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        user_name = ShopUser.objects.get(pk=self.kwargs.get('pk'))
        context['title'] = 'Админка. Удалить пользователя {}'.format(user_name.username)
        return context

    def delete(self, request, *args, **kwargs):
        user = ShopUser.objects.get(pk=self.kwargs.get('pk'))
        if request.method == 'POST':
            user.is_active = False
            user.save()
        return user


class UserUpdateView(UpdateView, IsSuperUserView):
    model = ShopUser
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin_custom:users')
    fields = '__all__'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        object_name = ShopUser.objects.get(pk=self.kwargs.get('pk')).username
        context['title'] = 'Админка. Редактирование {}.'.format(object_name)
        return context



