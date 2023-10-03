from django.shortcuts import render, HttpResponseRedirect
from django.contrib.messages import success, error
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
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

#function for shoppage
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

#function for aboutpage
def aboutPage(Request):
    return render(Request, "about.html")

#function for cartpage
@login_required(login_url="/login/")
def cartPage(Request):
    return render(Request, "cart.html")

#function for checkoutpage
@login_required(login_url="/login/")
def checkoutPage(Request):
    return render(Request, "checkout.html")

#function for confirmationpage
@login_required(login_url="/login/")
def confirmationPage(Request):
    return render(Request, "confirmation.html")

#function for contactpage
def contactPage(Request):
    return render(Request, "contact.html")

#function for loginpage
def loginPage(Request):
    if Request.method == "POST":
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(Request, user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/profile/")
        else:
            error(Request, "Invalid Username or Password!!!")
    return render(Request, "login.html")


#function for  signuppage
def signupPage(Request):
    if Request.method == "POST":
        password = Request.POST.get("password")
        cpassword = Request.POST.get("cpassword")
        if password == cpassword:
            email = Request.POST.get("email")
            username = Request.POST.get("username")
            name = Request.POST.get("name")
            try:
                User.objects.create_user(
                    username=username, email=email, password=password, first_name=name
                )
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


#function of profilepage
@login_required(login_url="/login/")
def profilePage(Request):
    if Request.user.is_superuser:
        return HttpResponseRedirect("/admin/")
    buyer = Buyer.objects.get(username=Request.user.username)
    wishlist = Wishlist.objects.filter(buyer=buyer)
    return render(Request, "profile.html", {"buyer": buyer,"wishlist":wishlist})
    

#function of updateprofilepage!
@login_required(login_url="/login/")
def updateProfilePage(Request):
    if(Request.user.is_superuser):
        return HttpResponseRedirect("/admin/")
    buyer = Buyer.objects.get(username=Request.user.username)
    if(Request.method=="POST"):
        buyer.name = Request.POST.get("name")
        buyer.emails = Request.POST.get("emails")
        buyer.phone = Request.POST.get("phone")
        buyer.address = Request.POST.get("address")
        buyer.pin = Request.POST.get("pin")
        buyer.city = Request.POST.get("city")
        buyer.state = Request.POST.get("state")
        if(Request.FILES.get("pic")):
            buyer.pic = Request.FILES.get("pic")
        buyer.save()
        return HttpResponseRedirect("/profile")
    return render(Request,"update-profile.html",{'buyer':buyer})

#Function will be single product
def singleProduct(Request, id):
    product = Product.objects.get(id=id)
    return render(Request, "single-product.html", {"product": product})

#function will be addtowishlist
@login_required(login_url="/login/")
def addtowishlistPage(Request,id):
    buyer = Buyer.objects.get(username=Request.user.username)
    product = Product.objects.get(id=id)
    try:
        w=Wishlist.objects.get(product=product,buyer=buyer)
    except:
        w= Wishlist()
        w.product= product
        w.buyer= buyer
        w.save() 
    return HttpResponseRedirect("/profile")   


#Use decorator function to inhance the function using wraping function.
@login_required(login_url="/login/")
def deletewishlist(Request,id):
    try:
        w =Wishlist.objects.get(id=id)
        w.delete()
    except:
        pass  

    return HttpResponseRedirect("/profile/")  














#logoutPage
def logoutPage(Request):
    logout(Request)
    return HttpResponseRedirect("/login/")
