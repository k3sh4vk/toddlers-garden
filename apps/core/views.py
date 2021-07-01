from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm

def homepage_view(request):
    return render(request, 'core/home.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Inquiry Received !')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = ContactForm()
        return render(request, 'core/contact.html', {'form': form})

def news_view(request):
    return render(request, 'core/news.html')

def playarea_view(request):
    return render(request, 'core/playarea.html')

def camp_view(request):
    return render(request, 'core/camp.html')

def room_view(request):
    return render(request, 'core/room.html')

def activities_view(request):
    return render(request, 'core/activities.html')
