from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    penpaper = Pen_Paper.objects.all()
    digital = Digital.objects.all()
    teammembers = Team.objects.all()
    moment = Moment.objects.all()
    return render(request, 'FAC/index.html',{'penpaper':penpaper, 'digital':digital, 'teammembers':teammembers, 'moment':moment})

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