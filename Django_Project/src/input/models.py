from django.db import models

# Create your models here.

class Student(models.Model):
	CATEGORIES=(
		('GE','GE'),
		('OBC','OBC'),
		('SC','SC'),
		('ST','ST')
	)
	BRANCHES=[
		('None','None'),
		('AE B.Tech','Aerospace Engineering B.Tech'),
		('CL B.Tech','Chemical Engineering B.Tech'),
		('CL Dual Deg','Chemical Engineering Dual Degree'),
		('CH','Chemistry'),
		('CE B.Tech','Civil Engineering B.Tech'),
		('CS B.Tech','Computer Science and Engineering B.Tech'),
		('EE B.Tech','Electrical Engineering B.Tech'),
		('EE Dual Deg E1','Electrical Engineering Dual Degree E1'),
		('EE Dual Deg E2','Electrical Engineering Dual Degree E2'),
		('EN Dual Deg','Energy Science and Engineering Dual Degree'),
		('EP B.Tech','Engineering Physics B.Tech'),
		('EP Dual Deg N1','Engineering Physics Dual Degree N1'),
		('ME B.Tech','Mechanical Engineering B.Tech'),
		('ME Dual Deg M2','Mechanical Engineering Dual Degree M2'),
		('MM B.Tech','Metallurgical Engineering B.Tech'),
		('MM Dual Deg Y1','Metallurgical Engineering Dual Degree Y1'),
		('MM Dual Deg Y2','Metallurgical Engineering Dual Degree Y2')
	]
	username =models.CharField(max_length=100,null=True)
	cpi = models.DecimalField(max_digits=4, decimal_places=2,null=True)
	category = models.CharField(max_length=100,choices=CATEGORIES, null=True)
	roll_number = models.CharField(max_length=9,primary_key=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	present_branch = models.CharField(max_length=100,choices=BRANCHES)
	preference_1=models.CharField(max_length=100,choices=BRANCHES)
	preference_2=models.CharField(max_length=100,choices=BRANCHES)
	preference_3=models.CharField(max_length=100,choices=BRANCHES)
	preference_4=models.CharField(max_length=100,choices=BRANCHES)
	preference_5=models.CharField(max_length=100,choices=BRANCHES)
	preference_6=models.CharField(max_length=100,choices=BRANCHES)
	preference_7=models.CharField(max_length=100,choices=BRANCHES)
	preference_8=models.CharField(max_length=100,choices=BRANCHES)
	preference_9=models.CharField(max_length=100,choices=BRANCHES)
	preference_10=models.CharField(max_length=100,choices=BRANCHES)
	preference_11=models.CharField(max_length=100,choices=BRANCHES)
	preference_12=models.CharField(max_length=100,choices=BRANCHES)
	preference_13=models.CharField(max_length=100,choices=BRANCHES)
	preference_14=models.CharField(max_length=100,choices=BRANCHES)
	preference_15=models.CharField(max_length=100,choices=BRANCHES)
	preference_16=models.CharField(max_length=100,choices=BRANCHES)

	def __unicode__(self):
		return self.first_name

class Test(models.Model):
	roll_number= models.CharField(max_length=9,primary_key=True)
	cpi = models.DecimalField(max_digits=4, decimal_places=2,null=True)

	def __unicode__(self):
		return self.roll_number

class Allotted(models.Model):
	serial=models.CharField(max_length=10,	primary_key=True)
	roll_number = models.CharField(max_length=20)
	name = models.CharField(max_length=100)
	present_branch = models.CharField(max_length=100)
	allotted_branch = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name


class Stats(models.Model):

	program = models.CharField(max_length=100,primary_key=True)
	cutoff = models.CharField(max_length=10,null=True)
	sanctionedStrength = models.IntegerField()
	originalStrength = models.IntegerField()
	finalStrength = models.IntegerField()

	def __unicode__(self):
		return self.program
