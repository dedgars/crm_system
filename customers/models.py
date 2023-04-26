from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)

    customer_type = models.CharField(max_length=100, blank=True)

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    organization_name = models.CharField(max_length=100, blank=True)
    organization_registration_number = models.CharField(max_length=100, blank=True)
    organization_vat_number = models.CharField(max_length=100, blank=True)

    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=False, unique=True)
    
    address = models.ForeignKey("Address", related_name='customer_addresses', on_delete=models.PROTECT)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.address}"


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)

    street_name = models.CharField(max_length=100, blank=True)
    street_number = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    neibourhood = models.CharField(max_length=100, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street_name} {self.street_number} {self.city}"