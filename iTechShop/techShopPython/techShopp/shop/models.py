from django.db import models


# Create your models here.
class PGroup(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    pro_id = models.AutoField(primary_key='true')
    pro_name = models.CharField(max_length=255)
    group = models.ForeignKey(PGroup, on_delete=models.CASCADE)
    pro_price = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    pro_image = models.ImageField(upload_to='shop_images')  # phải install 3rd party package: Pillow

    def __str__(self):
        return self.pro_id.__str__()



class Customer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    pnumber = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order(models.Model):
    cus = models.CharField(max_length=255)
    solddate = models.DateTimeField(auto_now_add=True)
    totmoney = models.IntegerField(default=0)


class OderDetail(models.Model):
    oderID = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)