from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, View
from typing import Any
from apps.users.forms import RegisterUserForm, AvtorizateUser
from apps.users.models import CustomUser, CustomUserManager
from django.contrib.auth import (
    authenticate as dj_auntheficate,
    login as dj_login,
    logout, authenticate, login)
from django.db.models import QuerySet
from django.contrib import messages


class RegisterUser(TemplateView):
    def get(self, request, *args: Any, **kwargs: Any):
        form = RegisterUserForm()
        return render(
            request=request,
            template_name='reg_log/register_scp.html',
            context={'form': form}
        )

    def post(self, request, *args: Any, **kwargs: Any) -> HttpResponse:
        template_name: str = 'reg_log/register_scp.html'
        form = RegisterUserForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                template_name,
                {'form': form}
            )

        user: CustomUser = form.save()
        email: str = form.cleaned_data['email']
        password: str = form.cleaned_data['password']
        user.email = email
        user.set_password(password)
        user.save()

        user: CustomUser = dj_auntheficate(email=email, password=password)
        if (not user) or (not user.is_active):
            return render(
                request,
                self.template_name
            )
        dj_login(request, user)
        users: QuerySet = CustomUser.objects.filter(**form.cleaned_data)
        return render(
            request,
            'primary/protect.html',
            {'users': users}
        )


class LoginView(FormView):
    template_name = 'reg_log/login.html'
    form_class = AvtorizateUser
    success_url = '/scp/add/'
    user = CustomUser

    def post(self, request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('add')
            else:
                messages.success(request, ('Неправильно введен логин или пароль'))
                return redirect('login')


def logout_user(request):
    logout(request)
    messages.success(request, ('Вы разлогинены'))
    return redirect('add')


def animationview(request):
    return render(
        request=request,
        template_name='reg_log/next_animation.html'
    )




    # def form_valid(self, form):
        # data = form.cleaned_data
        # user = dj_auntheficate(
        #     request=self.request,
        #     email=form.cleaned_data['email'],
        #     password=form.cleaned_data['password'],
        # )
        #
        # if user:
        #     login(self.request, user)
        #     return render(
        #         request=self.request,
        #         template_name='primary/protect.html',
        #         context={
        #             'form': form,
        #             'error': "Неверное имя пользователя или пароль"
        #         }
        #     )
        # else:
        #     form.add_error('__all__', 'Invalid credentials')
        #
        # return super().form_valid(form)




