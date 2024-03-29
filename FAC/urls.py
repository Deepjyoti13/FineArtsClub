from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('penpaper/', views.pen_paper, name="penpaper"),
    path('digital/', views.digital_art, name="digital"),
    path('moments/', views.ourmoments, name="moments"),
    path('notice/', views.notice, name="notice"),
    path('veterans/', views.veterans, name="veterans"),
    path('noticeboard/', views.noticeboard, name="noticeboard"),
    path('winners/', views.winners, name="winners"),
]
