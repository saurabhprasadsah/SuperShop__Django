from django.shortcuts import render,HttpResponseRedirect
from django.contrib.messages import success,error
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def homePage(Request):
    products = Product.objects.all().order_by("id")[0:12]
    return render(Request,'index.html',{'products':products})

# def shopPage(Request,mc,sc,br):
#     if(mc=="All" and sc=="All" and br=="All" ):
#         products= Product.objects.all().order_by("-id")
#     elif(mc!="All" and sc=="All" and br=="All"):
#         products= Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-id")

#     products = Product.objects.all()
#     maincategory = Maincategory.objects.all().order_by("-id")
#     subcategory = Subcategory.objects.all().order_by("-id")
#     brands = Brand.objects.all().order_by("-id")
#     return render(Request,"shop.html",{'products':products,'maincategory':maincategory,'subcategory':subcategory,'brands':brands,'mc':mc,'sc':sc,'br':br})

def shopPage(Request,mc,sc,br):
    if(mc=="All" and sc=="All" and br=="All"):
        products = Product.objects.all().order_by("-id")
    elif(mc!="All" and sc=="All" and br=="All"):
        products = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by("-id")
    elif(mc=="All" and sc!="All" and br=="All"):
        products = Product.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by("-id")
    elif(mc=="All" and sc=="All" and br!="All"):
        products = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("-id")
    elif(mc!="All" and sc!="All" and br=="All"):
        products = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by("-id").order_by("-id")
    elif(mc!="All" and sc=="All" and br!="All"):
        products = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by("-id").order_by("-id")
    elif(mc=="All" and sc!="All" and br!="All"):
        products = Product.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by("-id").order_by("-id")    
    else:
        products = Product.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by("-id").order_by("-id")    
    
    
    maincategory = Maincategory.objects.all().order_by("-id")
    subcategory = Subcategory.objects.all().order_by("-id")
    brand = Brand.objects.all().order_by("-id")

    # paginator = Paginator(products, 12)
    # page_number = Request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    return render(Request,"shop.html",{'products':products,'maincategory':maincategory,'subcategory':subcategory,'brand':brand,'mc':mc,'sc':sc,'br':br,})







def aboutPage(Request):
    return render(Request,"about.html")

def cartPage(Request):
    return render(Request,"cart.html")

def checkoutPage(Request):
    return render(Request,"checkout.html")

def confirmationPage(Request):
    return render(Request,"confirmation.html")

def contactPage(Request):
    return render(Request,"contact.html")

def loginPage(Request):
    return render(Request,"login.html")

#signup page
def signupPage(Request):
    if(Request.method == "POST"):
        password = Request.POST.get("password")     
        cpassword = Request.POST.get("cpassword")
        if(password==cpassword):
            email = Request.POST.get("email")
            username = Request.POST.get("username")
            User.create(username=username,email=email,password=password)
            name = Request.POST.get("name")
            phone = Request.POST.get("phone")
            b = Buyer()
            b.name = name  
            b.email = email
            b.username = username
            b.phone= phone
            b.save()
            return HttpResponseRedirect("/login")
        else:
            error(Request,"Password and cofirm Password Doesn't Matched!!!")        
    return render(Request,"signup.html")

def singleProduct(Request):
    return render(Request,"single-product.html")



