from django.urls import path, include
from . import views

from .views import Home, PostDetail, ProfileDetail, ProfileUpdate, CityDetail, PostCreate, PostDelete


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/signup/', views.Signup.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<slug:slug>/', ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cities/<int:pk>/', CityDetail.as_view(), name="city_detail"),
    path('cities/<slug:slug>', CityDetail.as_view(), name="city_detail"),
    path('posts/<int:city_pk>/create/', PostCreate.as_view(), name="post_create"),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name="post_delete") ,
]