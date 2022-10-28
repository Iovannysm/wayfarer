from django.shortcuts import redirect
from django.urls import path, include
from . import views

from .views import Home, PostDetail, ProfileDetail, ProfileUpdate, CityDetail, PostCreate, PostDelete, PostUpdate, About, CommentCreate, CommentDelete, CommentUpdate, SignupClean

# from .views import * -> will import everything including the imports on that page

# NOTE urls could be regrouped and organized 
urlpatterns = [
    path('', Home.as_view(), name='home'),# lambda req: redirect('accounts/signup/'), name='home'),
    path('accounts/signup/', SignupClean.as_view(), name='signup_clean'),
    # path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<slug:slug>/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('cities/<int:pk>/', CityDetail.as_view(), name='city_detail'),
    path('cities/<slug:slug>/', CityDetail.as_view(), name='city_detail'),
    path('posts/<int:pk>/create/<int:city_pk>/', PostCreate.as_view(), name='post_create'),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('posts/<int:pk>/update/', PostUpdate.as_view(), name= 'post_update'),
    path('about/', About.as_view(), name='about'),
    # comment should be comments for plural 
    path('posts/<int:pk>/comment/create/', CommentCreate.as_view(), name='comment_create'),
    # posts/<int:pk>/comment/<int:comment_pk>/delete
    path('comment/<int:pk>/delete/<int:post_pk>/', CommentDelete.as_view(), name='comment_delete'),
    path('comment/<int:pk>/update/', CommentUpdate.as_view(), name='comment_update')
]
