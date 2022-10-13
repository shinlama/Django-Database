from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from clubs.forms import ClubForm
from clubs.models import Club

# Create your views here.
def index(request):
    clubs = Club.objects.all()
    
    context = {
        'clubs': clubs,
    }
    return render(request, 'clubs/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            club = form.save()
            return redirect('clubs:detail', club.pk)
    else:
        form = ClubForm()
    context = {
        'form': form,
    }
    return render(request, 'clubs/create.html', context)



def detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    context = {
        'club': club
    }
    return render(request, 'clubs/detail.html', context)


@require_POST
def delete(request, pk):
    club = get_object_or_404(Club, pk=pk)
    club.delete()
    return redirect('clubs:index')


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    club = get_object_or_404(Club, pk=pk)
    
    if request.method == 'POST':
        
        form = ClubForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            form.save()
            return redirect('clubs:detail', club.pk)
    else:
        form = ClubForm(instance=club)
    context = {
        'club': club,
        'form': form,
    }
    return render(request, 'clubs/update.html', context)
