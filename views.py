from django.shortcuts import render
from .models import Product
# Create your views here.
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect


def index(request):
    
    p1=Product()
    p1.name="Shirt"
    p1.img="temp1.png"
    p1.price=500
    
    prods=[p1]
    return render(request,"products.html",{'pr':prods})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')
