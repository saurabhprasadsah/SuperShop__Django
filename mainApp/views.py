from django.shortcuts import render, HttpResponseRedirect
from django.contrib.messages import success, error
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *


# Create your views here.
def homePage(Request):
    products = Product.objects.all().order_by("id")[0:12]
    return render(Request, "index.html", {"products": products})


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


def shopPage(Request, mc, sc, br):
    if mc == "All" and sc == "All" and br == "All":
        products = Product.objects.all().order_by("-id")
    elif mc != "All" and sc == "All" and br == "All":
        products = Product.objects.filter(
            maincategory=Maincategory.objects.get(name=mc)
        ).order_by("-id")
    elif mc == "All" and sc != "All" and br == "All":
        products = Product.objects.filter(
            subcategory=Subcategory.objects.get(name=sc)
        ).order_by("-id")
    elif mc == "All" and sc == "All" and br != "All":
        products = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by(
            "-id"
        )
    elif mc != "All" and sc != "All" and br == "All":
        products = (
            Product.objects.filter(
                maincategory=Maincategory.objects.get(name=mc),
                subcategory=Subcategory.objects.get(name=sc),
            )
            .order_by("-id")
            .order_by("-id")
        )
    elif mc != "All" and sc == "All" and br != "All":
        products = (
            Product.objects.filter(
                maincategory=Maincategory.objects.get(name=mc),
                brand=Brand.objects.get(name=br),
            )
            .order_by("-id")
            .order_by("-id")
        )
    elif mc == "All" and sc != "All" and br != "All":
        products = (
            Product.objects.filter(
                brand=Brand.objects.get(name=br),
                subcategory=Subcategory.objects.get(name=sc),
            )
            .order_by("-id")
            .order_by("-id")
        )
    else:
        products = (
            Product.objects.filter(
                maincategory=Maincategory.objects.get(name=mc),
                subcategory=Subcategory.objects.get(name=sc),
                brand=Brand.objects.get(name=br),
            )
            .order_by("-id")
            .order_by("-id")
        )

    maincategory = Maincategory.objects.all().order_by("-id")
    subcategory = Subcategory.objects.all().order_by("-id")
    brand = Brand.objects.all().order_by("-id")

    # paginator = Paginator(products, 12)
    # page_number = Request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    return render(
        Request,
        "shop.html",
        {
            "products": products,
            "maincategory": maincategory,
            "subcategory": subcategory,
            "brand": brand,
            "mc": mc,
            "sc": sc,
            "br": br,
        },
    )


def aboutPage(Request):
    return render(Request, "about.html")


def cartPage(Request):
    return render(Request, "cart.html")


def checkoutPage(Request):
    return render(Request, "checkout.html")


def confirmationPage(Request):
    return render(Request, "confirmation.html")


def contactPage(Request):
    return render(Request, "contact.html")

def loginPage(Request):
    if(Request.method=="POST"):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(Request,user)
            if(user.is_superuser):
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/profile/")
        else:
            error(Request,"Invalid Username or Password!!!")
    return render(Request,"login.html")



# signup page
def signupPage(Request):
    if (Request.method == "POST"):
        password = Request.POST.get("password")
        cpassword = Request.POST.get("cpassword")
        if password == cpassword:
            email = Request.POST.get("email")
            username = Request.POST.get("username")
            name = Request.POST.get("name")
            try:
                User.objects.create_user(username=username, email=email, password=password, first_name=name)
                phone = Request.POST.get("phone")
                b = Buyer()
                b.name = name
                b.email = email
                b.username = username
                b.phone = phone
                b.save()
                return HttpResponseRedirect("/login/")
            except:
                error(Request, "UserName already taken!!!")
        else:
            error(Request, "Password and cofirm Password Doesn't Matched!!!")
    return render(Request, "signup.html")



def profilePage(Request):
    if(Request.user.is_superuser):
        return HttpResponseRedirect("/admin/")
    username = Request.user.username
    try:
        buyer = Buyer.objects.get(username=username)
        return render(Request,"profile.html",{'buyer':buyer})
    except:
        return HttpResponseRedirect("/login/")    
    

def updateProfile(Request):
    if(Request.user.is_superuser):
        return HttpResponseRedirect("/admin/")
    username = Request.user.username
    try:
        buyer = Buyer.objects.get(username=username)
        if(Request.method=="POST"):
            buyer.name = Request.POST.get("name")
            buyer.email = Request.POST.get("email")
            buyer.phone = Request.POST.get("phone")
            buyer.city = Request.POST.get("city")
            buyer.state = Request.POST.get("state")
            buyer.pin = Request.POST.get("pin")
            buyer.address = Request.POST.get("address")
            if(Request.FILES.get("pic")):
                buyer.name= Request.FIELS.get("pic")
            buyer.save()     
            return HttpResponseRedirect("/profile")
        return render(Request,"update-profile.html",{'buyer':buyer})
    except:
        return HttpResponseRedirect("/login/")   

    

def singleProduct(Request, id):
    product = Product.objects.get(id=id)
    return render(Request, "single-product.html", {"product": product})


def logoutPage(Request):
    logout(Request)
    return HttpResponseRedirect("/login/")
