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
    path('cart/',mainApp.cartPage, name="cart"),
    path('confirmation/',mainApp.confirmationPage, name="confirmation"),
    path('contact/',mainApp.contactPage, name="contact"),
    path('login/',mainApp.loginPage, name="login"),
    path('signup/',mainApp.signupPage, name="signup"),

    path('shop/',mainApp.shopPage, name="shop"),
    path('single-Product/',mainApp.singleProduct, name="single-Product"),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) 
