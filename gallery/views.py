from django.shortcuts import render, redirect
from .models import Picture

# Create your views here.

def display(request):
    pictures = Picture.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        
        for image in images:
            picture = Picture.objects.create(
                image=image,
            )

        return redirect('index')

    return render(request, 'gallery/gallery.html', {'pictures':pictures})


def show(request, pk):
    picture = Picture.objects.get(id=pk)
    return render(request, 'gallery/show.html', {'picture': picture})