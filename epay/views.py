from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import MySQLdb as mysql
from django.db import connection
from epay.queries import *
import json
from epay.serializers import *
from epay.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from epay import forms
from rest_framework import viewsets
from MySQLdb.cursors import SSDictCursor
from django.core.mail import send_mail
from epay.models import *
import urllib , urllib2 
from django.utils import timezone
# Create your views here.
@api_view(['POST'])
def pay_now(request):
	utoken=request.POST["user"]
	amount=request.POST["amount"]
	url="http://roadrunner.com/e-auth"
	data={'token':utoken}
	req=urllib2.Request(url , data)
	res=urllib2.urlopen( req)
	return HttpResponse(res)
	


