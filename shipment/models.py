from django.contrib.auth import get_user_model
from django.db import models


class Shipment(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    Shipment = [('fedexAIR', 'fedexAIR'), ('fedexGroud', 'fedexGroud'), ('PSExpress', 'PSExpress'), ('UPS2DAY', 'UPS2DAY')]

    carrierServiceID = models.CharField(max_length=255, choices=Shipment)
    width = models.IntegerField(blank=False, null=False)
    height = models.IntegerField(blank=False, null=False)
    length = models.IntegerField(blank=False, null=False)
    weight = models.IntegerField(blank=False, null=False)



    def __str__(self):
        return self.carrierServiceID
