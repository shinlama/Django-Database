from multiprocessing import context
from re import search
from select import select
from django.shortcuts import render, redirect, get_object_or_404
from clubs.models import Club

from users.forms import UserForm
from .models import User
from django.db.models import Q
from django.views.decorators.http import require_http_methods, require_POST
# Create your views here.


def index(request):

    print(request.GET)

    search = request.GET.get('search')
    selected_type = request.GET.get('selected_type')

    if search is not None:
        users = User.objects.filter(Q(first_name__contains = search)|Q(country__contains=search))
        if selected_type == 'country':
            users = User.objects.filter(country__contains = search)
        else:
            users = User.objects.filter(first_name__contains = search )
    
    else:
        users = User.objects.all()
    context = {
        'users':users
    }

    return render(request, 'users/index.html', context)

def profile(request, pk):
    person = get_object_or_404(User, pk=pk)
    context = {
        'person': person,
    }
    return render(request, 'users/profile.html', context)

def club_signup(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        print(request.POST)
        user.clubs.add(request.POST.get('club'))
        return redirect('users:profile', user.pk)
    else: 
        clubs = Club.objects.all()
    context = {
        'user': user,
        'clubs': clubs,
    }
    return render(request, 'users/club_signup.html', context)

    