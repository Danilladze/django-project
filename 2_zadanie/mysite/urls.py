from django.contrib import admin
from django.urls import path, include, re_path
from mysite.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('links/',views.link_show, name='links'),
    re_path('^(?P<pk>\d+)/delete/', views.LinkDeleteView.as_view(), name='delete'),
    path('create_link/', views.create, name ='create_link')
]
