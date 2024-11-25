from django.shortcuts import render,redirect
from home.models import Movie

def home(request):

    m=Movie.objects.all()

    return render(request,'home_page.html',{"movie":m})

def movie_details(request,i):

    m = Movie.objects.get(id=i)

    return  render(request,'movie_details.html',{"movie":m})

def add_movie(request):
    if(request.method == 'POST'):
        name=request.POST.get('mname')
        image= request.FILES["mimg"]
        lang=request.POST.get('lang')
        det=request.POST.get('det')

        c=Movie.objects.create(name=name,image=image,language=lang,details=det)
        c.save()
        return redirect('home:home')

    return render(request,'add_movie.html')

def edit_movie(request,k):
    m = Movie.objects.get(id=k)
    if(request.method == 'POST'):
        m.name = request.POST.get('mname')
        m.image = request.FILES["mimg"]
        m.language = request.POST.get('lang')
        m.details = request.POST.get('det')
        m.save()
        return redirect('home:home')
    return render(request,'edit_movie.html',{"movie":m})


def delete_movie(request,d):
    k = Movie.objects.get(id=d)
    k.delete()
    return home(request)