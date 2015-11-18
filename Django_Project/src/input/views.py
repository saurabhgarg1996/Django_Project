from django.shortcuts import render
from login.forms import *
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from .forms import StudentForm
from .models import Student
from django.http import HttpResponseRedirect
# Create your views here.
BRANCHES={
	'None':'None',
	'AE B.Tech':'Aerospace Engineering B.Tech',
	'CL B.Tech':'Chemical Engineering B.Tech',
	'CL Dual Deg':'Chemical Engineering Dual Degree',
	'CH':'Chemistry',
	'CE B.Tech':'Civil Engineering B.Tech',
	'CS B.Tech':'Computer Science and Engineering B.Tech',
	'EE B.Tech':'Electrical Engineering B.Tech',
	'EE Dual Deg E1':'Electrical Engineering Dual Degree E1',
	'EE Dual Deg E2':'Electrical Engineering Dual Degree E2',
	'EN Dual Deg':'Energy Science and Engineering Dual Degree',
	'EP B.Tech':'Engineering Physics B.Tech',
	'EP Dual Deg N1':'Engineering Physics Dual Degree N1',
	'ME B.Tech':'Mechanical Engineering B.Tech',
	'ME Dual Deg M2':'Mechanical Engineering Dual Degree M2',
	'MM B.Tech':'Metallurgical Engineering B.Tech',
	'MM Dual Deg Y1':'Metallurgical Engineering Dual Degree Y1',
	'MM Dual Deg Y2':'Metallurgical Engineering Dual Degree Y2'
}
CATEGORIES={
	'GE':'GE',
	'OBC':'OBC',
	'SC':'SC',
	'ST':'ST'
}
def fillform_view(request):
	if request.user.is_authenticated() and request.user.username != "admin":
		if request.method == 'POST' :
			s_form=StudentForm(request.POST)
			if s_form.is_valid():
				try:
					users=Student.objects.get(roll_number=s_form.cleaned_data['roll_number'])		
				except Student.DoesNotExist :			#save new roll number and delete previous if one user 1 roll number
					s_model=s_form.save()
					s_model.username=request.user.username			#get username of logged in user
					s_model.category=s_form.cleaned_data['category']
					s_model.present_branch=s_form.cleaned_data['present_branch']
					s_model.preference_1=s_form.cleaned_data['preference_1']
					s_model.preference_2=s_form.cleaned_data['preference_2']
					s_model.preference_3=s_form.cleaned_data['preference_3']
					s_model.preference_4=s_form.cleaned_data['preference_4']
					s_model.preference_5=s_form.cleaned_data['preference_5']
					s_model.preference_6=s_form.cleaned_data['preference_6']
					s_model.preference_7=s_form.cleaned_data['preference_7']
					s_model.preference_8=s_form.cleaned_data['preference_8']
					s_model.preference_9=s_form.cleaned_data['preference_9']
					s_model.preference_10=s_form.cleaned_data['preference_10']
					s_model.preference_11=s_form.cleaned_data['preference_11']
					s_model.preference_12=s_form.cleaned_data['preference_12']
					s_model.preference_13=s_form.cleaned_data['preference_13']
					s_model.preference_14=s_form.cleaned_data['preference_14']
					s_model.preference_15=s_form.cleaned_data['preference_15']
					s_model.preference_16=s_form.cleaned_data['preference_16']
					s_model.save()
					# print("hello")
					return HttpResponseRedirect('/thanks/')
			else:
				t=StudentForm(
				{
				'roll_number':s_form.data['roll_number'],
				'first_name':s_form.data['first_name'],
				'last_name':s_form.data['last_name'],
				'cpi':s_form.data['cpi'],
				'username':s_form.data.get('username')

				},
				category_shift=s_form.data['category'],
				branch_remove_present=s_form.data['present_branch'],
				branch_remove_1=s_form.data['preference_1'],
				branch_remove_2=s_form.data['preference_2'],
				branch_remove_3=s_form.data['preference_3'],
				branch_remove_4=s_form.data['preference_4'],
				branch_remove_5=s_form.data['preference_5'],
				branch_remove_6=s_form.data['preference_6'],
				branch_remove_7=s_form.data['preference_7'],
				branch_remove_8=s_form.data['preference_8'],
				branch_remove_9=s_form.data['preference_9'],
				branch_remove_10=s_form.data['preference_10'],
				branch_remove_11=s_form.data['preference_11'],
				branch_remove_12=s_form.data['preference_12'],
				branch_remove_13=s_form.data['preference_13'],
				branch_remove_14=s_form.data['preference_14'],
				branch_remove_15=s_form.data['preference_15'],
				branch_remove_16=s_form.data['preference_16']
				)
				b=True

				return render(request,'fillform.html',{'s':t,'bool':b})
				# raise :roll no already taken, enter another
			#raise invalid data

		else :
			try:
				users=Student.objects.get(username=request.user.username)		
			except Student.DoesNotExist :
				s=StudentForm()						
				b=False							#if a user has not filled the bc form
				return render(request,'fillform.html',{'s':s,'bool':b})					#yet then blank form is supplied
			#you have already filled the form ----redirect
			#BRANCHES=[]

			return HttpResponseRedirect('/update/')	

			#if s.is_valid():				# if unbound (if we use initial)so we cant validate
			# print(s.non_field_errors)		#gives non field errors
																#else previous filled form is supplied for updation			
			# BRANCHES = [i for i in s.cleaned_data['present_branch'].field.choices if i[0] != tmp]
				#  print("fuckk off")
			# s.cleaned_data['present_branch'].field.choices=BRANCHES
	



	else:
		return HttpResponseRedirect('/home')

def thanks_view(request):
	if request.user.is_authenticated():
		return render(request,'thanks.html',{})
	else:
		return HttpResponseRedirect('/home')

def update_view(request):
	if request.user.is_authenticated() and request.user.username != "admin":
		if request.method=='POST':
			users=Student.objects.get(username=request.user.username)
			key_category=users.category
			key_present=users.present_branch
			key_1=users.preference_1
			key_2=users.preference_2
			key_3=users.preference_3
			key_4=users.preference_4
			key_5=users.preference_5
			key_6=users.preference_6
			key_7=users.preference_7
			key_8=users.preference_8
			key_9=users.preference_9
			key_10=users.preference_10
			key_11=users.preference_11
			key_12=users.preference_12
			key_13=users.preference_13
			key_14=users.preference_14
			key_15=users.preference_15
			key_16=users.preference_16

			# tupl=(tmp_key,tmp_value)
			# print(tupl)
			# tmp=[]
			# tmp.append(tupl)
			s=StudentForm(
				{
				'username':users.username,
				'roll_number':users.roll_number,
				'first_name':users.first_name,
				'last_name':users.last_name,
				'cpi':users.cpi
				# 'present_branch':users.present_branch,

				},

				category_shift=key_category,branch_remove_present=key_present,branch_remove_1=key_1,branch_remove_2=key_2,branch_remove_3=key_3,branch_remove_4=key_4,branch_remove_5=key_5,branch_remove_6=key_6,branch_remove_7=key_7,branch_remove_8=key_8,branch_remove_9=key_9,branch_remove_10=key_10,branch_remove_11=key_11,branch_remove_12=key_12,branch_remove_13=key_13,branch_remove_14=key_14,branch_remove_15=key_15,branch_remove_16=key_16

			)		#branch_remove is argument passed to constructor of StudentForm										
			users.delete()
			b=True
			return render(request,'fillform.html',{'s':s,'bool':b})		

		else:
			return render(request,"login_data.html",{'data': Student.objects.get(username=request.user.username)})
	else:
		return HttpResponseRedirect('/home')