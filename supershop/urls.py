"""
URL configuration for supershop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp import views as mainApp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.homePage, name="home"),
    path('about/',mainApp.aboutPage, name="about"),
    path('checkout/',mainApp.checkoutPage, name="checkout"),
    
    path('add-to-cart/',mainApp.addtocartPage, name="add-to-cart"),
    path('cart/',mainApp.cartPage, name="cart"),

    path('delete-cart/<str:id>/',mainApp.deletecartPage, name="delete-cart"),



    path('confirmation/',mainApp.confirmationPage, name="confirmation"),
    path('contact/',mainApp.contactPage, name="contact"),
    path('login/',mainApp.loginPage, name="login"),
    path('logout/',mainApp.logoutPage, name="logout"),

    path('signup/',mainApp.signupPage, name="signup"),
    path('profile/',mainApp.profilePage, name="profile"),

    path('update-profile/',mainApp.updateProfilePage, name="updateProfile"),

    path('add-to-wishlist/<int:id>/',mainApp.addtowishlistPage, name="add-to-wishlist"),

    path('delete-wishlist/<int:id>/',mainApp.deletewishlist, name="deletewishlist"),






    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shopPage, name="shop"),

    path('single-product/<int:id>',mainApp.singleProduct, name="single-Product"),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 
