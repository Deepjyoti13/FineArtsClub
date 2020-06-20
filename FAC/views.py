from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    penpaper = Pen_Paper.objects.all()
    digital = Digital.objects.all()
    teammembers = Team.objects.all()
    moment = Moment.objects.all()
    notes = Notice.objects.all()
    return render(request, 'FAC/index.html',{'penpaper':penpaper, 'digital':digital, 'teammembers':teammembers, 'moment':moment, 'notes':notes})

def pen_paper(request):
    penpaper = Pen_Paper.objects.all()
    context = {'penpaper':penpaper}
    return render(request, 'FAC/penpaper.html', context)

def digital_art(request):
    digital = Digital.objects.all()
    context = {'digital':digital}
    return render(request, 'FAC/digital.html', context)

def team(request):
    teammembers = Team.objects.all()
    context = {'teammembers':teammembers}
    return render(request, 'FAC/team.html', context)

def ourmoments(request):
    moment = Moment.objects.all()
    context = {'moment':moment}
    return render(request, 'FAC/momentgallery.html', context)

def notice(request):
    notes = Notice.objects.all()
    context = {'notes':notes}
    return render(request, 'FAC/notice.html', context)

def veterans(request):
    formers = Team.objects.all()
    context = {'formers':formers}
    return render(request, 'FAC/veterans.html', context)

def noticeboard(request):
    boards = Notice.objects.all()
    context = {'boards':boards}
    return render(request, 'FAC/noticeboard.html', context)

def winners(request):
    win = Winner.objects.all()
    context = {'win':win}
    return render(request, 'FAC/winners.html', context)