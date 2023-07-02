from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATE_CHOICES=(
    ('تهران','تهران'),
    ('مشهد','مشهد'),
    ('اصفهان','اصفهان'),
    ('شیراز','شیراز'),
    ('تبریز','تبریز'),
    ('کرج','کرج'),
    ('اهواز','اهواز'),
    ('کرمانشاه','کرمانشاه'),
    ('ارومیه','ارومیه'),
    ('رشت','رشت'),
    ('زاهدان','زاهدان'),
    ('همدان','همدان'),
    ('کرمان','کرمان'),
    ('یزد','یزد'),
    ('اردبیل','اردبیل'),
    ('بندرعباس','بندرعباس'),
    ('اراک','اراک'),
    ('اسلامشهر','اسلامشهر'),
    ('زنجان','زنجان'),
    ('سنندج','سنندج'),
    ('قزوین','قزوین'),
    ('خرم‌آباد','خرم‌آباد'),
    ('گرگان','گرگان'),
    ('ساری','ساری'),
    ('آبادان','آبادان'),
    ('ورامین','ورامین'),
    ('شهرکرد','شهرکرد'),
    ('سمنان','سمنان'),
    ('مرودشت','مرودت'),
    ('زابل','زابل'),
    ('یاسوج','یاسوج'),
    ('خرمشهر','خرمشهر'),
    ('بم','بم'),
    ('بانه','بانه'),
    ('چابهار','چابهار'),
    ('لاهیجان','لاهیجان'),
    ('چالوس','چالوس'),
)

CATEGORY_CHOICE=(
    ('AJ','آجیل مخلوط'),
    ('PE','پسته'),
    ('BA','بادام'),
    ('GE','گردو'),
    ('FA','فندق'),
    ('TO','تخمه'),
    ('NO','نخود'),

)
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField(max_length=200)
    discounted_price=models.FloatField()
    quantity=models.FloatField(max_length=200)
    type=models.CharField(max_length=500)
    category=models.CharField(choices=CATEGORY_CHOICE ,max_length=2)
    product_image=models.ImageField(upload_to='product')
    
    def __str__(self) : 
        return self.name

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile=models.IntegerField(default=0)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price 