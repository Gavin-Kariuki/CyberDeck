from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import Image


# Create your views here.
def karibu(request):
    return render(request, 'index.html')

def mapicha(request):
    images = Image.display_all_images()
    return render(request,'all-images/mapicha.html',{"images":images},)

def picha(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,'all-images/image.html',{"image":image})

def search_results(request):
    if 'tafutapicha' in request.GET and request.GET['tafutapicha']: #tafutapicha is what i will name my search element tag in the templates
        category = request.GET.get('tafutapicha')
        images_searched = Image.search_by_category(category)
        message = f"{category}"
        print(images_searched)
        return render(request, 'all-images/tafuta.html',{"message":message,"images":images_searched})
    else:
        message = "No search results available"
        return render(request,'all-images/tafuta.html',{"message":message})



