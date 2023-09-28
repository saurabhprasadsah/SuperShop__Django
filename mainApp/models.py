from django.db import models

# Create your models here.
class Maincategory(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=30,unique=True)

    def __str__(self):  
        return str(self.id)+" /"+self.name


class Subcategory(models.Model):
    id = models.AutoField(primary_key= True, unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)+" /"+self.name  


class Brand(models.Model):
    id = models.AutoField(primary_key= True, unique=True)
    name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to= "uploads/brand")


    def __str__(self):
        return str(self.id)+" /"+self.name
    


class Product(models.Model):
    id = models.AutoField(primary_key= True, unique=True)
    name = models.CharField(max_length=30)
    maincategory = models.ForeignKey(Maincategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    baseprice = models.IntegerField()
    discount = models.IntegerField()
    finalprice = models.IntegerField()
    stock = models.BooleanField(default=True)
    color = models.CharField(max_length=30)
    size = models.CharField(max_length=10)
    description = models.TextField(default="")
    pic1 = models.ImageField(upload_to= "uploads/product")
    pic2 = models.ImageField(upload_to= "uploads/product",default=None, blank=True, null= True)
    pic3 = models.ImageField(upload_to= "uploads/product",default=None, blank=True, null= True)
    pic4 = models.ImageField(upload_to= "uploads/product",default=None, blank=True, null= True)

    def __str__(self):
        return str(self.id)+" /"+self.name
    

class Buyer(models.Model):
      id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=30)
      username =models.CharField(max_length=30, unique=True)
      emails = models.EmailField(max_length=30)
      phone= models.CharField(max_length=11,default="")
      address =models.TextField(default="",null=True, blank=True)
      pin = models.IntegerField(default=None,null=True, blank=True)
      city = models.CharField(max_length=50,default="",null=True, blank=True)
      state= models.CharField(max_length=50,default="",null=True, blank=True)
      pic =models.ImageField(upload_to="uploads/users",default="",null=True, blank=True)

      def __str__(self):
          return str(self.id)+" / "+self.name+" / "+self.username
          






