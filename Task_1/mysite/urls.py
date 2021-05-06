from django.contrib import admin
from django.urls import path, include, re_path
from mysite.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('links/',views.link_show, name='links'),
    path('delete_link/<link_id>', views.delete_link, name='delete_link'),
    path('delete_all_links/<link_id>', views.delete_all_links, name='delete_all_links'),
    path('create_link/', views.create, name ='create_link')
]
