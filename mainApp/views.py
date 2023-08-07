from django.shortcuts import render
from django.contrib.messages import success,error
from .models import *

# Create your views here.
def homePage(Request):
    return render(Request,'index.html')

def shopPage(Request):
    return render(Request,"shop.html")

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


def signupPage(Request):
     if(Request.method =="POST"):
        password = Request.POST.get("password")     
        cpassword = Request.POST.get("cpassword")
        if(password==cpassword):
            username = Request.POST.get("username")
            email = Request.POST.get("email")

            name = Request.POST.get("name")
            phone = Request.POST.get("phone")
        else:
            error(Request,"Password and cofirm Password Doesn't Matched!!!")   
            
     return render(Request,"signup.html")

def singlePage(Request):
    return render(Request,"single-product.html")


