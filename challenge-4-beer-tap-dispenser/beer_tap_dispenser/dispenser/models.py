from django.db import models
import uuid



class Dispenser(models.Model):
    BEER_PRICE_PER_LITRE = 12.25
    
    unique_id = models.UUIDField(null=False, default=uuid.uuid4, editable=False, unique=True)
    flow_volume = models.FloatField(null=False)
    

    @property
    def amount(self):
        amount = 0
        for usage in self.usages.all():
            amount += usage.total_spent
        return amount

    @property
    def status(self):
        last_usage = self.usages.last()
        if last_usage is not None and last_usage.closed_at is None:
            return 'open'
        return 'close'

    @property
    def updated_at(self):
        last_usage = self.usages.last()
        if last_usage is None:
            return None
        if last_usage.closed_at is not None:
            return last_usage.closed_at
        return last_usage.opened_at

    def __str__(self):
        return str(self.unique_id)


class Usage(models.Model):
    opened_at =  models.DateTimeField(null=False)
    closed_at = models.DateTimeField(null=True)
    flow_volume = models.FloatField(null=False)
    total_spent = models.FloatField(null=False, default=0)
    dispenser = models.ForeignKey(Dispenser, related_name='usages', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.dispenser) + " - " + str(self.opened_at) 