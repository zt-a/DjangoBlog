from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# Create your views here.
def index(request):
    blogs = BlogModel.objects.all().order_by('-time_create')
    context = {
        'blogs': blogs,
    }
    return render(request, 'main/index.html', context=context)


# def loginView(request):
#     form = LoginUserForm
#     user = form.save()
#     login(request, user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'main/login.html', context=context)
#
#
# def signUp(request):
#     form = RegisterUserForm
#     context = {
#         'form': form,
#     }
#     return render(request, 'main/signup.html', context=context)


class SignUpView(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_success_url(self):
        reverse_lazy('login')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    success_url = reverse_lazy('home')
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def categoriesView(request):
    categories = Category.objects.filter(is_published=True)
    context = {
        'categories': categories,
    }
    return render(request, 'main/categories.html', context=context)


def aboutView(request):
    return render(request, 'main/about.html')


def contactView(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
    else:
        form = ContactUsForm()
    if form.is_valid():
        form.save()
        redirect('home')

    context = {
        'title': 'Обратная связь',
        'form': form,
    }
    return render(request, 'main/contact.html', context=context)


def searchView(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data['query']
        results = BlogModel.objects.filter(title__icontains=query)

    context = {
        'form': form,
        'results': results,
    }
    return render(request, 'main/search.html', context=context)


def postCategoriesView(request, slug):
    category = get_object_or_404(Category, slug=slug)
    context = {
        'category': category,
    }
    return render(request, 'main/post_categories.html', context=context)

def postTagView(request, slug):
    tag = get_object_or_404(TagModel, slug=slug)
    context = {
        'tag': tag,
    }
    return render(request, 'main/post_tag.html', context=context)


def BlogVeiw(request):
    blogs = BlogModel.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'main/blogs.html', context=context)


def tagsView(request):
    tags = TagModel.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'main/tags.html', context=context)


@login_required
def profileView(request):
    return render(request, 'main/profile.html')


class ProfileView(LoginRequiredMixin, ListView):
    # def get(self, request):
    #     return render(request, 'accounts/profile.html')
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'main/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    # fields = '__all__'
    template_name = 'main/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'main/delete_profile.html'
    success_url = reverse_lazy('logout')

    def get_object(self, queryset=None):
        return self.request.user


def logout_user(request):
    logout(request)
    return redirect('login')

# class AddBlog(CreateView):
#     form_class = BlogForm
#     template_name = 'main/addblog.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Добавление блога'
#         return context

def addBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Устанавливаем автора блога
            blog.save()
            return redirect('blogs')  # Перенаправляем пользователя на страницу списка блогов
    else:
        form = BlogForm()
    context = {
        'form': form,
    }
    return render(request, 'main/addblog.html', context=context)

def blogPostView(request, slug):
    blog = get_object_or_404(BlogModel, slug=slug)
    context = {
        'blog': blog,
    }
    return render(request, 'main/blog_post.html', context=context)