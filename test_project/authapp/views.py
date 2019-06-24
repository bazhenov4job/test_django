from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from .models import ShopUser
from .forms import ShopUserRegisterForm
from django.contrib import auth
from django.urls import reverse, reverse_lazy

# Create your views here.


def login(request):
    title = 'вход'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            # Выбрасывает нас обратно на глагне
            return HttpResponseRedirect(reverse('main'))


    """login_form = ShopUserLoginForm(data=request.POST)"""
    """if request.method == "POST" and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))"""

    """content = {'title': title, 'login_form': login_form}"""
    return render(request, 'authapp/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = ShopUserRegisterForm()

    context = {'form': register_form}
    return render(request, 'authapp/register.html', context)


class EditView(UpdateView):
    model = ShopUser
    template_name = 'authapp/register.html'
    fields = 'username', 'avatar', 'email'
    success_url = reverse_lazy('main')

