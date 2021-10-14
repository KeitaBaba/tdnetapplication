from django.db import models

class Tekijikaiji(models.Model):
    code = models.IntegerField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    company_title = models.TextField(blank=True, null=True)
    pdf = models.TextField(blank=True, null=True)
    disclosure_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tekijikaiji'


class Customer(models.Model):
    customer_address = models.TextField(primary_key=True)
    customer = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'



