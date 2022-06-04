from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from user.forms import LoginForm


class HomeView(TemplateView):
    template_name = 'layout/base.html'


class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['form'] = LoginForm()
        return context

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'back_url' in request.POST:
                        return redirect(request.POST['back_url'])
                    return redirect(reverse('product_list'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
