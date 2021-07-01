from django.shortcuts import render, redirect


def homepage_view(request):
    return render(request, 'core/home.html')

def contact_view(request):
    return render(request, 'core/contact.html')

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
