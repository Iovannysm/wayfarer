from django.db.models.base import Model
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse  
from main_app.models import Comment, Profile, Post, City

from datetime import datetime

# import the class that will handle basic views
from django.views import View

# auth imports
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Forms
from .forms import SignUpForm, CreatePostForm
from django.http import HttpResponse

# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=SignUpForm()
        return context
    
class ProfileDetail(DetailView):
    model = Profile
    template_name = "profile_detail.html"

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['name', 'current_city']
    template_name = "profile_update.html"
    def get_success_url(self):
        return reverse("profile_detail", kwargs={'pk': self.object.pk})

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.filter(user = Profile)
        return context

# Signup view
class SignupClean(View):
    def get(self, request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'home.html', context)
    
    def post(self, request):
        form = SignUpForm(request.POST)
        name = request.POST.get('username')
        slug = request.POST.get('username')
        
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user, name=name, slug=slug)

            login(request, user)
            return redirect("profile_detail", pk=profile.pk)
        else:
            context = {"form": form}
            return render(request, "404.html", context)

class Signup(View):
    def get(self, request, **kwargs):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, "home.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        name = request.POST.get("name")
        city = request.POST.get("current_city")
        image = request.POST.get("profile_picture")
        
        
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(name=name, current_city=city, profile_picture=image, user=user)

            login(request, user)
            return redirect("profile_detail", pk=profile.pk)
        else:
            context = {"form": form}
            return render(request, "home.html", context)

class CityDetail(DetailView):
    model = City
    template_name = "city_detail.html"
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['form'] = CreatePostForm()
        context['cities'] = City.objects.all()
        context['now'] = datetime.now()
        return context

# @method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    def post(self, request, pk, city_pk):
        # form = CreatePostForm(request.POST)
        try:
            # if form.is_valid():
            title = request.POST['post-title']
            content = request.POST['post-content']
            city = City.objects.get(pk=city_pk)
            profile = request.user.profile
            Post.objects.create(title=title, content=content,city=city, profile=profile)
            return redirect('city_detail', pk=city_pk)
        except Exception as error:
            return render(request, "city_detail")
            

@method_decorator(login_required, name='dispatch')
class PostDelete(View):
    def post(self, request, pk):
        Post.objects.filter(pk=pk).delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))

@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'city_detail.html'

    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.object.city.pk})

class About(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"]=SignUpForm()
        return context

class CommentCreate(CreateView):
    def post(self, request, pk):
        content = request.POST.get("comment-content")
        profile = request.user.profile
        post = Post.objects.get(pk=pk)
        Comment.objects.create(content=content, profile=profile, post=post)
        return redirect('post_detail', pk=pk)

class CommentDelete(View):
    def post(self, request, pk, post_pk):
        Comment.objects.filter(pk = pk).delete()
        return redirect("post_detail", pk=post_pk)

class CommentUpdate(UpdateView):
    model = Comment
    fields = ["content"]

    def get_success_url(self):
        return reverse("post_detail", kwargs={'pk':self.object.post.pk} )
