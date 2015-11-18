from django import forms
from django.forms import ModelForm
from .models import Student
from django.contrib.auth.models import User
import random	
from .models import Test
from django.utils.translation import ugettext_lazy as _
CATEGORIES=(
	('GE','GE'),
	('OBC','OBC'),
	('SC','SC'),
	('ST','ST')
)
BRANCHES_dict={
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
CATEGORIES_dict={
	'GE':'GE',
	'OBC':'OBC',
	'SC':'SC',
	'ST':'ST'
}
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
def get_branches(BRANCHES,branch):
	TEMP=BRANCHES[:]
	if branch:
		TEMP = [i for i in TEMP if i[0]!=branch]
		TEMP.insert(0,(branch,BRANCHES_dict[branch]))
	# print(TEMP)
	return TEMP

def get_category(CATEGORIES,cat):
	TEMP=CATEGORIES[:]
	if cat:
		TEMP = [i for i in TEMP if i[0]!=cat]
		TEMP.insert(0,(cat,CATEGORIES_dict[cat]))
	# print(TEMP)
	return TEMP

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields =['roll_number','first_name','last_name','cpi']
	    # error_messages = {						#custom error message of each field
	    #         'roll_number': {
	    #             'max_length': _("This writer's name is too long."),
	    #         },
	    #     }


	# category=forms.ChoiceField(choices=CATEGORIES, required =True)
	# present_branch=forms.ChoiceField(choices=BRANCHES,required=True)

	def __init__(self, *args, **kwargs):				#constructor called everytime the form is created i.e. form is created
		category_shift=kwargs.pop('category_shift',None)		
		branch_remove_present=kwargs.pop('branch_remove_present',None)
		branch_remove_1=kwargs.pop('branch_remove_1',None)
		branch_remove_2=kwargs.pop('branch_remove_2',None)
		branch_remove_3=kwargs.pop('branch_remove_3',None)
		branch_remove_4=kwargs.pop('branch_remove_4',None)
		branch_remove_5=kwargs.pop('branch_remove_5',None)
		branch_remove_6=kwargs.pop('branch_remove_6',None)
		branch_remove_7=kwargs.pop('branch_remove_7',None)
		branch_remove_8=kwargs.pop('branch_remove_8',None)
		branch_remove_9=kwargs.pop('branch_remove_9',None)
		branch_remove_10=kwargs.pop('branch_remove_10',None)
		branch_remove_11=kwargs.pop('branch_remove_11',None)
		branch_remove_12=kwargs.pop('branch_remove_12',None)
		branch_remove_13=kwargs.pop('branch_remove_13',None)
		branch_remove_14=kwargs.pop('branch_remove_14',None)
		branch_remove_15=kwargs.pop('branch_remove_15',None)
		branch_remove_16=kwargs.pop('branch_remove_16',None)

		super(StudentForm, self).__init__(*args, **kwargs)
		self.fields['category']= forms.ChoiceField(choices=get_category(CATEGORIES,category_shift),required=True)
		self.fields['present_branch'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_present),required=False)
		self.fields['preference_1'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_1),required=False)
		self.fields['preference_2'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_2))
		self.fields['preference_3'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_3))
		self.fields['preference_4'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_4))
		self.fields['preference_5'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_5))
		self.fields['preference_6'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_6))
		self.fields['preference_7'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_7))
		self.fields['preference_8'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_8))
		self.fields['preference_9'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_9))
		self.fields['preference_10'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_10))
		self.fields['preference_11'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_11))
		self.fields['preference_12'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_12))
		self.fields['preference_13'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_13))
		self.fields['preference_14'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_14))
		self.fields['preference_15'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_15))
		self.fields['preference_16'] = forms.ChoiceField(choices=get_branches(BRANCHES,branch_remove_16))

	def clean_roll_number(self):
		try:
			try:
				exist=Student.objects.get(roll_number=self.cleaned_data['roll_number'])
				raise forms.ValidationError(_("Roll Number Has already applied"))
			except Student.DoesNotExist :
				user=Test.objects.get(roll_number=self.cleaned_data['roll_number'])
				return self.cleaned_data['roll_number']
		except Test.DoesNotExist :
			raise forms.ValidationError(_("Please Enter a valid Roll Number"))

	def clean_cpi(self):
		if (self.cleaned_data['cpi']<0.00 or self.cleaned_data['cpi']> 10.00) :
			raise forms.ValidationError(_("Please Enter a valid CPI"))
		else:
			return self.cleaned_data['cpi']

	def clean(self):
		cleaned_data = super(StudentForm, self).clean()
		if 'roll_number' in self.cleaned_data and 'cpi' in self.cleaned_data:
			try:
				user=Test.objects.get(roll_number=self.cleaned_data['roll_number'])
				if(user.cpi!=self.cleaned_data['cpi']) :
					print()
					raise forms.ValidationError(_("CPI and Roll Number don't  match"))
			except Test.DoesNotExist :
				raise forms.ValidationError(_("Please Enter a valid Roll Number"))
			return self.cleaned_data

	def clean_present_branch(self):
		if(self.cleaned_data['present_branch']=="None"):
			raise forms.ValidationError(_("Branch is Required"))
		else:
			return self.cleaned_data['present_branch']

	# def clean_preference_1(self):
	# 	if(self.cleaned_data['preference_1']=="None"):
	# 		raise forms.ValidationError(_("Atleast 1 Preference is Required"))
	# 	else:
	# 		return self.cleaned_data['preference_1']