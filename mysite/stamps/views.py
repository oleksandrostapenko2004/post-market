from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from .models import *
from .forms import *
from .utils import *

# menu = ['Про сайт', 'Новини', 'Де моє замовлення?']
menu = [{'title': 'Кошик', 'url_name': 'basket'},
        {'title': 'Новини', 'url_name': 'news'},
        {'title': 'Зворотній зв\'язок', 'url_name': 'contact'},
        {'title': 'Де моє замовлення?', 'url_name': 'where_order'},
        {'title': 'Увійти', 'url_name': 'login'}]

class StampHome(DataMixin, ListView):
    model = Stamp
    template_name = 'stamps/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Усі товари')
        context = dict(list(context.items()) + list(c_def.items()))
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Stamp.objects.filter().select_related('cat')

class StampCategory(DataMixin, ListView):
    model = Stamp
    template_name = 'stamps/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Stamp.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Категорія: " + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class ShowPost(DataMixin, DetailView):
    model = Stamp
    template_name = 'stamps/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class WhereOrder(LoginRequiredMixin, DataMixin, CreateView):
    form_class = WhereOrderForm
    template_name = 'stamps/where_order.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Де моє замовлення?')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# class RegisterUser(DataMixin, CreateView):
#     form_class = RegisterUserForm
#     template_name = 'stamps/register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Реєстрація')
#         context = dict(list(context.items()) + list(c_def.items()))
#         return context
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('home')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'stamps/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Реєстрація')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'stamps/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизація')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):
        return reverse_lazy('home')

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'stamps/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Зворотній зв\'язок')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

def logout_user(requests):
    logout(requests)
    return redirect('login')

class StampNews(DataMixin, ListView):
    model = Stamp
    template_name = 'stamps/news.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):

        c_def = self.get_user_context(title='Новини')

        return c_def

class StampBasket(DataMixin, ListView):
    model = Stamp
    template_name = 'stamps/basket.html'
    context_object_name = 'basket'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Кошик')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class MakeOrderFormView(DataMixin, FormView):
    form_class = MakeOrderForm
    template_name = 'stamps/make_order.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Оформлення замовлення')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

class SuccessfulOrder(DataMixin, ListView):
    model = Stamp
    template_name = 'stamps/successful_order.html'
    context_object_name = 'successful_order'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Успішно виконане замовлення')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# def index(requests):
#     posts = Stamp.objects.all()
#     cats = Category.objects.all()
#     context = {'menu': menu,
#                'cats': cats,
#                'title': 'Усі товари',
#                'posts': posts,
#                'cat_selected': 0}
#     return render(requests, 'stamps/index.html', context=context)

def about(requests):
    posts = Stamp.objects.all()
    return render(requests, 'stamps/about.html', {'menu': menu,
                                                  'title': 'Про сайт',
                                                  'posts': posts})

def basket(requests):
    return HttpResponse("Кошик")

def news(requests):
    return render(requests, 'stamps/news.html')

def contact(requests):
    return HttpResponse("Зворотній зв'язок")

# def login(requests):
#     return HttpResponse("Авторизація")

# def order(requests):
#     return HttpResponse("Де моє замовлення?")

# def show_post(requests, post_slug):
#     post = get_object_or_404(Stamp, slug=post_slug)
#     context = {'menu': menu,
#                'post': post,
#                'title': post.title,
#                'cat_selected': post.cat_id}
#     return render(requests, 'stamps/post.html', context=context)

# def show_category(requests, cat_id):
#     posts = Stamp.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#     context = {'menu': menu,
#                'cats': cats,
#                'title': '',
#                'posts': posts,
#                'cat_selected': cat_id}
#     return render(requests, 'stamps/index.html', context=context)

def categories(requests, cat_id):
    return HttpResponse(f"<h1>Товари по категоріях</h1>{cat_id}")

def where_order(requests):
    if requests.method == 'POST':
        form = WhereOrderForm(requests.POST, requests.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.add_error(None, "Замовлення не знайдено")
    else:
        form = WhereOrderForm()
    context = {'form': form, 'menu': menu, 'title': 'Де моє замовлення?'}
    return render(requests, 'stamps/where_order.html', context=context)

def pageNotFound(requests, exception):
    return HttpResponseNotFound("<h1>Сторінку не знайдено</h1>")
