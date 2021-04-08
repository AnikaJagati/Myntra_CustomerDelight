from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from .models import Product
import cv2 as cv

uploaded_file_url = ''

prod1 = Product()
prod1.name = 'ZARA Smocked Top'
prod1.id = 1001
prod1.price = 999.0
prod1.img = 'ZaraSmock.jpeg'
prod1.ptype = "Tops"


prod2 = Product()
prod2.name = 'Vero Moda Smocked Top'
prod2.id = 1002
prod2.price = 1099.0
prod2.img = 'VMSmock.jpeg'
prod2.ptype = "Tops"


prod3 = Product()
prod3.name = 'Addidas T-shirt'
prod3.id = 1003
prod3.price = 899.0
prod3.img = 'ADt.jpeg'
prod3.ptype = "T-Shirts"


prod4 = Product()
prod4.name = 'Baggit Satchel Bag'
prod4.id = 1004
prod4.price = 1399.0
prod4.img = 'Bag.png'
prod4.ptype = "Bags"


prod5 = Product()
prod5.name = 'Lavie Baguette'
prod5.id = 1005
prod5.price = 2999.0
prod5.img = 'Lavie.jpeg'
prod5.ptype = "Bags"


prod6 = Product()
prod6.name = 'ONLY Striped Spaghetti Top'
prod6.id = 1006
prod6.price = 1499.0
prod6.img = 'Spaghetti2.jpeg'
prod6.ptype = "Tops"


prod7 = Product()
prod7.name = 'US-POLO T-shirt'
prod7.id = 1007
prod7.price = 1999.0
prod7.img = 'USPOLO.jpeg'
prod7.ptype = "T-shirts"


prod8 = Product()
prod8.name = 'Forever New Spaghetti Top '
prod8.id = 1008
prod8.price = 1299.0
prod8.img = 'FNSpaghetti.jpeg'
prod8.ptype = "Tops"


prod9 = Product()
prod9.name = 'H&M Spaghetti Top'
prod9.id = 1009
prod9.price = 1599.0
prod9.img = 'HMSpaghetti.jpg'
prod9.ptype = "Tops"



prod10 = Product()
prod10.name = 'H&M Spaghetti Top'
prod10.id = 1009
prod10.price = 1599.0
prod10.img = 'HMSpaghetti2.jpeg'
prod10.ptype = "Tops"

products = [prod1,prod2,prod3,prod4,prod5,prod6,prod8,prod9,prod10]

# Create your views here.
def open(request):

    return render(request,'index.html')

def draw(request):
    return render(request,'myDrawingapp.html')

def view_products(request):
    return render(request,'products.html',{'allProducts':products})

def simple_upload(request):
    global uploaded_file_url
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
        'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')


def check_results(request):
    global uploaded_file_url
    global products

    productsToBeDisplayed = []
    pathNew = 'C:/Users/Kaushiki/projects/project1'+uploaded_file_url
    for i in range(len(products)):

        
        prodPath=products[i].img
        ProductpathNew = 'C:/Users/Kaushiki/projects/project1/static/product_images/'+prodPath
        
        
        template_path = r"{}".format(pathNew)
        product_path=r"{}".format(ProductpathNew)
        print(product_path)
        print(template_path)

        imgg= cv.imread(template_path,0)

        
        
        img=imgg
        edges = cv.Canny(img,100,200)
        img = cv.imread(product_path,0)
        edges1 = cv.Canny(img,100,200)
        img = edges1
        img2 = img.copy()
        
        template=edges
        w, h = template.shape[::-1]
        
        methods = ['cv.TM_CCOEFF_NORMED']
        for meth in methods:
            img = img2.copy()
            method = eval(meth)
            area=1
            # Apply template Matching
            res = cv.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            # If the method is TM_COEFF_NORMED  take maximum
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            rec=cv.rectangle(img,top_left, bottom_right, (255,255,255), 2)
            
            
            print("max:",max_val)
            
           
            if(max_val<0.06):
                productsToBeDisplayed.append(products[i])

    print(len(productsToBeDisplayed))
        
    return render(request, 'index-2.html',{'productsToBeDisplayed':productsToBeDisplayed})

