from django.db import models

# Create your models here.

APPLIANCES = [('Gas boiler', 'Gas boiler'), 
              ('Hot water heater', 'Hot water heater'), 
              ('Hot water tank', 'Hot water tank'),
              ('Thermostat', 'Thermostat'),
              ('Other', 'Other')]

BRANDS = [('Bosch', 'Bosch'), 
          ('Junkers', 'Junkers'), 
          ('Viessmann', 'Viessmann'),
          ('Valiant', 'Valiant'),
          ('Other', 'Other ')]


class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, choices=APPLIANCES, default='Gas boiler')
    brand = models.CharField(max_length=100, choices=BRANDS, default='Junkers')
    model = models.CharField(max_length=100, blank=True)
    serial_number = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey("customers.Customer", related_name='customer_equipment', on_delete=models.PROTECT)
    address = models.ForeignKey("customers.Address", related_name='address_equipment', on_delete=models.PROTECT)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.brand} {self.model}'