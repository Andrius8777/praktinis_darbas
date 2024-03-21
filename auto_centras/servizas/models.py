from django.db import models
import datetime
import decimal
from django.utils import timezone

    
class Mechanic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class ClientData(models.Model):
    client_name = models.CharField(max_length=150, verbose_name='Vardas')
    phone_number = models.CharField(max_length=15, verbose_name='Tel. nr.:')
    make = models.CharField(max_length=100, verbose_name='Markė:')
    model = models.CharField(max_length=100, verbose_name='Modelis:')
    number_plate = models.CharField(max_length=10, verbose_name='Tr. pr. nr.:')
    vin_number = models.CharField(max_length=17, verbose_name='Vin numeris:')
    current_year = datetime.date.today().year
    start_year = 1990
    if current_year < start_year:
        current_year = start_year
    year = models.IntegerField(verbose_name='Pagaminimo metai:')
    engine_type = models.CharField(max_length=10, verbose_name='Variklio tipas:')
    driven_axle = models.CharField(max_length=10, verbose_name='Varančioji ašis:')
    body_type = models.CharField(max_length=12, verbose_name='Kėbulo tipas:')
    gearbox_type = models.CharField(max_length=10, verbose_name='Pavarų dėžė:')
    engine_power_choices = [(kw, kw) for kw in range(40, 401)]
    engine_power_kw = models.IntegerField(choices=engine_power_choices, verbose_name='Variklio galia:')
    engine_capacity_choices = [
        (decimal.Decimal(str(litre)), decimal.Decimal(str(litre))) 
        for litre in [round(0.1 * i, 1) for i in range(9, 61)]
    ]
    engine_capacity = models.DecimalField(max_digits=3, decimal_places=1, choices=engine_capacity_choices, verbose_name='Variklio darbinis tūris:')
    issue_notes = models.TextField(blank=True, null=True, verbose_name='Vizito priežastis:')
    ordered_parts_description = models.TextField(blank=True, null=True, verbose_name='Užsakytos dalys:')
    ordered_parts_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Užsakytų dalių kaina:')
    mechanic = models.ForeignKey(Mechanic, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Darbus atliko:')
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Įkainis už remontą:')
    repair_notes = models.TextField(blank=True, null=True, verbose_name='Mechaniko išvados:')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client_name}'s {self.make} {self.model}"
    
    def total_price(self):
        return self.labor_cost + self.ordered_parts_price
    
    @property
    def invoice_number(self):
        current_year = str(timezone.localtime(timezone.now()).year)[-2:]
        client_id = f"{self.pk:04}"
        return f"VAC{current_year}{client_id}"