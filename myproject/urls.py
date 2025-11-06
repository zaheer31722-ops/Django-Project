"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.home, name='home'),
    # path('contact/',views.contact, name='contact'),
    # path('about/', views.About.as_view(), name='about'),
    path('user/<str:username>/',views.profile, name='user-profile'),
    path('product/<int:id>/',views.product_detail, name='product-detail'),
    path('blog/<slug:slug>/',views.blog_post, name='blog-post'),
    path('item/<uuid:item_id>/', views.item_detail, name='item-detail'),
    path('media/<path:path_file>/', views.media_handler, name='media_handler'),
    path('post/', views.go_to_post, name='go_to_post'),
    path('',include('myapp.urls')),
]
