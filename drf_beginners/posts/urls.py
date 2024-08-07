"""
URL configuration for drf_beginners project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from . import views
from .views import PostView

urlpatterns = [

    path('', PostView.as_view(), name='view_posts'),  # resouce for  all posts,
    path('<int:id>/', PostView.as_view(), name='post-detail'),
    # path('search',views.view_post_by_id,name='search posts'),
    # # path('create',views.create_post,name='create post'),
    # path('delete',views.delete_post,name='delete post'),
    # path('update',views.update_post,name='update post')
]
