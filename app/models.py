from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Ssj(models.Model):
    name = models.CharField(max_length=155, blank=True)
    hospcode = models.CharField(max_length=5, default='00068')

    def __str__(self):
        return self.name +' - '+self.hospcode

    class Meta:
        ordering = ('name',)
        verbose_name = 'จังหวัด'
        verbose_name_plural = 'จังหวัด'
 
class Reponse_kpi(models.Model):
    name = models.CharField(max_length=155, blank=True )
    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)
        verbose_name = 'กลุ่มงาน'
        verbose_name_plural = 'กลุ่มงาน'
        
class Profile(models.Model):

    type_list = (   ('admin','ผู้ดูแลระดับจังหวัด'),
                    ('input','ผู้รับผิดชอบตัวชี้วัด'),
                    ('leader','หัวหน้าฝ่าย'),
                )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, choices=type_list, default='input')
    user_phone = models.CharField(max_length=100, blank=True, null=True)
    ssj = models.ForeignKey(Ssj, on_delete=models.CASCADE)
    response_kpi = models.ForeignKey(Reponse_kpi, on_delete=models.CASCADE)

    def __str__(self):
        return  self.user.first_name +' - '+ str(self.ssj)

    class Meta:
        ordering = ('user',)
        verbose_name = 'ข้อมูลผู้ใช้'
        verbose_name_plural = 'ข้อมูลผู้ใช้'

class Kpi(models.Model):
    kpi_code = models.CharField(max_length=15, unique=True)
    kpi_name = models.TextField(blank=True)
    kpi_group = models.CharField(max_length=15, blank=True)
    response_kpi = models.ForeignKey(Reponse_kpi, on_delete=models.CASCADE)
    goal = models.CharField(max_length=11, blank=True)
    goal_descript = models.TextField(blank=True)
    cri_type = models.CharField(max_length=15, blank=True)
    unit = models.CharField(max_length=55, blank=True)
    formular = models.CharField(max_length=55, blank=True)
    formular_type = models.CharField(max_length=15, blank=True)
    descript_a = models.TextField(blank=True)
    descript_b = models.TextField(blank=True)

    def __str__(self):
        return self.kpi_code+' - '+self.kpi_name

    class Meta:
        ordering = ('kpi_code',)
        verbose_name = 'ตัวชี้วัด KPI'
        verbose_name_plural = 'ตัวชี้วัด KPI'
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'หมวดหมู่สินค้า'
        verbose_name_plural = 'หมวดหมู่สินค้า'
    

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'สินค้า'
        verbose_name_plural = 'สินค้า'
        
class KeyInput(models.Model):
    year_list = (('2020', '2563'),)

    kpi = models.ForeignKey(Kpi, on_delete=models.CASCADE)
    hospcode = models.ForeignKey(Ssj, default='00068', on_delete=models.CASCADE)
    response = models.ForeignKey(Reponse_kpi, default='1', on_delete=models.CASCADE)
    year = models.CharField(max_length=6, choices=year_list, default='2019')
    a1 = models.CharField(max_length=55, blank=True)
    b1 = models.CharField(max_length=55, blank=True)
    a2 = models.CharField(max_length=55, blank=True)
    b2 = models.CharField(max_length=55, blank=True)
    a3 = models.CharField(max_length=55, blank=True)
    b3 = models.CharField(max_length=55, blank=True)
    a4 = models.CharField(max_length=55, blank=True)
    b4 = models.CharField(max_length=55, blank=True)
    a5 = models.CharField(max_length=55, blank=True)
    b5 = models.CharField(max_length=55, blank=True)
    a6 = models.CharField(max_length=55, blank=True)
    b6 = models.CharField(max_length=55, blank=True)
    a7 = models.CharField(max_length=55, blank=True)
    b7 = models.CharField(max_length=55, blank=True)
    a8 = models.CharField(max_length=55, blank=True)
    b8 = models.CharField(max_length=55, blank=True)
    a9 = models.CharField(max_length=55, blank=True)
    b9 = models.CharField(max_length=55, blank=True)
    a10 = models.CharField(max_length=55, blank=True)
    b10 = models.CharField(max_length=55, blank=True)
    a11 = models.CharField(max_length=55, blank=True)
    b11 = models.CharField(max_length=55, blank=True)
    a12 = models.CharField(max_length=55, blank=True)
    b12 = models.CharField(max_length=55, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_update = models.DateTimeField(default = timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(KeyInput, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.kpi)+' - '+ str(self.response) +' - '+str(self.hospcode) +' - '+str(self.user)

    class Meta:
        ordering = ('kpi',)
        verbose_name = 'บันทึก KPI'
        verbose_name_plural = 'บันทึก KPI'

class Club(models.Model):
    name = models.CharField(max_length=200)
    money = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.name, self.money)
    