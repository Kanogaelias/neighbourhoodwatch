from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood,Profile,Business,Post
from .forms import NewNeighbourhoodForm,NewProfileForm,NewBusinessForm,NewPostForm
from django.views import generic

@login_required(login_url='/accounts/login/')
def home(request):
   neighbourhood=Neighbourhood.objects.all()
   return render(request,'index.html',{"neighbourhood":neighbourhood,})
@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = current_user
            neighbourhood.save()
        return redirect('Home')

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})
def  neighbourhood_details(request,neighbourhood_id):

    businesses=Business.objects.filter(neighborhood=neighbourhood_id)
    posts=Post.objects.filter(neighborhood=neighbourhood_id)
    neighbourhood=Neighbourhood.objects.get(pk=neighbourhood_id)
    return render(request,'details.html',{'neighbourhood':neighbourhood,'businesses':businesses,'posts':posts,})

@login_required(login_url="/accounts/login/")

def profile(request):
    profiles=Profile.objects.filter(user=request.user.id)
    neighbourhood=Neighbourhood.objects.filter(admin=request.user.id)
    return render (request,'profile.html',{'neighbourhood':neighbourhood,'profiles':profiles,})
@login_required(login_url="/accounts/login/")

def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        profile_form = NewProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        profile_form = NewProfileForm()
    return render(request, 'new_profile.html', {"profile_form": profile_form,})

def search_hoods(request):

    if 'neighborhood' in request.GET and request.GET['neighborhood']:
        search_term=request.GET.get('neighborhood')
        searched_hoods=Neighbourhood.search_by_name(search_term)
        message=f'{search_term}'

        return render(request,'search.html',{"message":message,"neighborhood":searched_hoods,})

    else:
        message='You Havent searched for any term'

        return render(request, 'search.html',{"message":message,})
@login_required(login_url="/accounts/login/")

def new_business(request,pk):
    current_user = request.user
    neighborhood = get_object_or_404(Neighbourhood,pk=pk)
    if request.method == 'POST':
        business_form = NewBusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = current_user
            business.neighborhood=neighborhood
            business.save()
        return redirect('detail', neighbourhood_id=neighborhood.id)

    else:
        business_form = NewBusinessForm()
    return render(request, 'new_business.html', {"form": business_form,'neighborhood':neighborhood})

@login_required(login_url="/accounts/login/")

def new_post(request,pk):
    current_user = request.user
    neighborhood = get_object_or_404(Neighbourhood,pk=pk)
    if request.method == 'POST':
        post_form = NewPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = current_user
            post.neighborhood=neighborhood
            post.save()
        return redirect('detail', neighbourhood_id=neighborhood.id)

    else:
        post_form = NewPostForm()
    return render(request, 'new_post.html', {"form": post_form,'neighborhood':neighborhood})