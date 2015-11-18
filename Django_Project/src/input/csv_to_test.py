from .models import Test
import csv
import os
from django.http import HttpResponseRedirect

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILE_DIR= os.path.join(BASE_DIR, "input/data.csv")

def upload(request):
	with open(FILE_DIR) as csvf:
		row = csv.reader(csvf, delimiter=',', quotechar='|')
		for myrow in row:
			myrow[1]=float(myrow[1].strip(' "'))			
			tmp=Test(myrow[0],myrow[1])
			tmp.save()
	return HttpResponseRedirect('/thanks')

def delete(request):
	query=Test.objects.all()
	query.delete()
	return HttpResponseRedirect('/thanks')