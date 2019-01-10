from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Profile,Business,Post
from .forms import NewNeighbourhoodForm,NewProfileForm,NewBusinessForm,NewPostForm
from django.views import generic

@login_required(login_url='/accounts/login/')
def home(request):
   neighbourhood=Neighbourhood.objects.all()
   return render(request,'index.html',{"neighbourhood":neighbourhood,})
