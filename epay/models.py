from __future__ import unicode_literals
from bus.models import Ticket
from taxi.models import Booking
from runner.models import User
from django.utils.encoding import python_2_unicode_compatible
STATUS_CHOICES=(
	("DONE","DONE"),
	("LATER","LATER"))

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Payment(model.Model):
	id=models.AutoField(primary_key=True)
	user=models.ForeignKey(User , models.DO_NOTHING , related_name="+",null=True)
	ticket=models.ForeignKey(Ticket , models.DO_NOTHING , related_name="+",null=True)
	booking=models.ForeignKey(Booking , models.DO_NOTHING , related_name="+",null=True)
	transaction_date=models.DateTimeField()
	amount=models.IntegerField(default=0)
	token=models.CharField(max_length=200,default="")
	status=models.CharField(max_length=20,default="",choices=STATUS_CHOICES)
	def __str__(self):
		return self.user.name+" "+str(transaction_date)

@python_2_unicode_compatible
class Wallet(models.Model):
	id=models.AutoField(primary_key=True)
	user=models.ForeignKey(User , models.DO_NOTHING , related_name="+",null=True)
	transaction_date=models.DateTimeField()
	amount=models.IntegerField(default=0)
	token=models.CharField(max_length=200,default="")
	def __str__(self):
		return self.user.name+" "+str(transaction_date)

	

