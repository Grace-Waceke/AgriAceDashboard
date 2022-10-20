from django.db import models

# Create your models here.

class Farmer(models.Model):
    COMPANY_CHOICES=(
        ('ADC Molo','ADC Molo'),
        ('KARLO,Tigoni','KARLO,Tigoni'),
        ('Kisima Farm','Kisima Farm'),
        ('Agrico East Africa','Agrico East Africa'),
        ('Fresh Crop Limited','Fresh Crop Limited'),
        ('Singus Enterprise ','Singus Enterprise '),
        ('Egerton University Unit','Egerton University Unit'),
        ('GTIL (Apical cuttings and minitubers only','Apical cuttings and minitubers only'),
        ('Aberdare Technology Limited','Aberdare Technology Limited'),
        ('Gene Biotech seeds LTD','Gene Biotech seeds LTD'),
        ('Sigen Hortipruse Ltd','Sigen Hortipruse Ltd'),
        ('Kevian Kenya seeds (Kirinyaga seeds)','Kevian Kenya seeds (Kirinyaga seeds)'),
        ('Savannah Fresh Hort. Farmers Cooperative Society Ltd','Savannah Fresh Hort. Farmers Cooperative Society Ltd'),
        ('Mahindra and Mahindra s.Africa Ltd','Mahindra and Mahindra s.Africa Ltd'),
        ('Baraka Agricultural College (Nakuru)','Baraka Agricultural College (Nakuru)'),
    )
    company_name = models.CharField(null=True,choices=COMPANY_CHOICES,max_length=100)
    customer_id=models.CharField(null=True,max_length=8)
    phonenumber =models.CharField (max_length=12)
    ORDERS_CHOICES=(
        ('Shangii','Shangii'),
        ('Dutch robijn', 'Dutch robijn'),
        ('Sherekea', 'Sherekea'),
        ('Konjo','Konjo'),
        ('Lady Amarilla','Lady Amarilla'),
        ('Musica','Musica'),
    )
    orders = models.CharField(null=True,choices=ORDERS_CHOICES,max_length=100)
    STATUS_CHOICES=(
        ('Delivered','Delivered'),
        ('Pending','Pending'),
        ('In Progress','In Progress'),
    )
    status = models.CharField(null=True,choices=STATUS_CHOICES,max_length=100)
  
   

