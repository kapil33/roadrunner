from __future__ import unicode_literals
from bus.models import Ticket
from taxi.models import Booking
from runner.models import User
STATUS_CHOICES=(
	("DONE","DONE"),
	("LATER","LATER"))

from django.db import models

# Create your models here.
class Wallet(model.Model):
	id=models.AutoField(primary_key=True)
	user=models.ForeignKey(User , models.DO_NOTHING , related_name="+",null=True)
	ticket=models.ForeignKey(Ticket , models.DO_NOTHING , related_name="+",null=True)
	booking=models.ForeignKey(Booking , models.DO_NOTHING , related_name="+",null=True)
	transaction_date=models.DateTimeField()
	amount=models.IntegerField(default=0)
	token=models.CharField(max_length=200,default="")
	status=models.CharField(max_length=20,default="",choices=STATUS_CHOICES)