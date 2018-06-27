from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView

from chat.forms import LoginForm, MessageCreateForm, ChatRegistrationForm
from chat.models import Message


class ChatView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/chat.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['messages'] = Message.objects.all().order_by('-id')
        return data
# Create your views here.


class MyLoginView(View):
    def get(self, request, *args, **kwargs):
        # request - То что получаем от пользователя в запросе
        form = LoginForm()
        # компилируем объект Template -> рендерим контекст
        return render(request, 'login.html', {'form': form})
    # запрос, файл шаблона, место куда добавляем для использования в шаблоне

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)  # данные, переданные пользователем

        # Проверка формы на загрузку
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # проверка на существование такого пользователя
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect(reverse('chat_get'))
            # reverse - возращает абс. ссылку из chat\urls.py
            # Возвращает перенаправление на URL указанный через аргументы.

        return render(request, 'login.html', {'form': form, 'form_action': reverse('login')})


class ChatLoginView(LoginView):
    template_name = 'login.html'  # в ContextData есть form, так что не прописываем
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form_action'] = reverse('login')  # в urls
        return data

    def get_success_url(self):
        return reverse('chat_get')
# при использовании reverse url's не привязаны к путям->
# можем менять как угодно

# Logout на подобии с LogIn надо написать


class MessageCreateView(CreateView):
    form_class = MessageCreateForm

    def get_success_url(self):
        return reverse('chat_get')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['post'])

    def form_invalid(self, form):
        return HttpResponseBadRequest(reverse('chat_get'))


class ChatLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))


class ChatRegistrationView(FormView):
    form_class = ChatRegistrationForm
    template_name = "formReg.html"

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
