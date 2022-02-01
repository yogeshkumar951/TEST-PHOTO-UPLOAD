from django.shortcuts import render

from test_app.models import Product

# Create your views here.
def index(request):
    try:
        if  request.method == 'POST':

            product = Product.objects.create(
            name = request.POST['name'],
            color = request.POST['color'],
            description = request.POST['decription'],
            price = request.POST['price'],
            image = request.FILES['image']
        )
            msg = 'your data has been sent'
            return render(request,'index.html',{'msg':msg,'product':product})

        else:
            msg = 'something went wrong'
            return render(request,'index.html',{'msg':msg})
    except:
        return render(request,'index.html')



def Show_image(request):
    product = Product.objects.all()


    return render(request,'show_image.html',{'product':product})
    

