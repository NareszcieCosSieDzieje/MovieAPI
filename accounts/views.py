from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import mixins, generics
from .forms import CreateUserForm
from .models import Account
from .serializers import AccountSerializer


def registration_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form: CreateUserForm = CreateUserForm()
    if request.method == 'POST':
        form: CreateUserForm = CreateUserForm(request.POST)
        if form.is_valid():
            user: User = User()
            user.username = form.cleaned_data.get('username')
            password: str = form.cleaned_data.get('password1')
            user.set_password(password)
            user.email = form.cleaned_data.get('email')
            user.save()
            Account(user=user).save()
            username: str = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('accounts:accounts-login')
        else:
            messages.error(request, form.error_messages)
    context: dict = {'form': form}
    return render(request, "accounts/register/index.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    context: dict = {}
    if request.method == 'POST':
        username: str = request.POST.get('username')
        password: str = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, f"Invalid data for username: {username}")
    return render(request, "accounts/login/index.html", context)


@login_required(login_url='accounts:accounts-login')
def logout_view(request):
    logout(request)
    return redirect("home")


class AccountList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Account.objects.none()
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.filter(user_id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AccountDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

        queryset = Account.objects.none()
        serializer_class = AccountSerializer

        def get_queryset(self):
            return Account.objects.filter(user_id=self.request.user.id)

        def get(self, request, *args, **kwargs):
            return self.retrieve(request, *args, **kwargs)

        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            logout(request)
            return self.destroy(request, *args, **kwargs)
