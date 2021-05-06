from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import link
from .forms import LinkForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from tldextract import extract
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Главная страница
@login_required
def home(request):
    link_form = LinkForm()
    create(request)
    return render(request, 'home.html', {'link_form':link_form})

# Создания линка
def create(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            Link = form.cleaned_data['link']
            link_value_check(Link)
    form = LinkForm()

    data = {
        'forma':form
    }

    return render(request,'create_link.html',data) 

# Удаление линка
def delete_link(request, link_id):
    Link = link.objects.get(pk = link_id)
    Link.delete()
    return redirect('links')

# Удаление всех линков
def delete_all_links(request, link_id):
    Link = link.objects.all()
    Link.delete()
    return redirect('links')


# Постраничный вывод линков
@login_required
def link_show(request):
    all_links = link.objects.order_by('-id')

    p = Paginator(all_links, 10)
    
    page_num = request.GET.get('page',1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    return render(request, 'links_list.html', {'all_links': page})


# Регистрация
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})



# Проверка правильности линка

class MyException(Exception):
    pass

def link_value_check(link):
    tsd, td, tsu = extract(link)
    domain_zone = ["ru","com","org","xyz","ua","рф"]
    if tsu in domain_zone:
        pass
    # except:
    #     raise MyException("msg here")