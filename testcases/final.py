import os, random, sys
import csv
import math

dict = {}			#Name vs. code dictionary
br = {}				# Name vs branch object dictionary

#---------------  Base class : Student (Stores - CPI, Current Branch Number, Preference List, Roll Number) -----------#
class Student:

	def __init__(self, roll, cpi, curr, pref, name, cat):
		self.name = name
		self.curr = curr
		self.roll = roll
		self.cpi = cpi
		self.pref = pref
		self.lower = -1
		self.prev = curr
		self.orig = curr
		self.cat = cat

	def update(self, branch):
		self.curr = branch
		self.pref = self.pref[0:self.pref.index(dict2[self.curr])];
		br[dict2[branch]].lowestcpi = self.cpi 
	
#----------------- Class: Branch , Stores details of each branch------------------------------------ #
class Branch:
	def __init__(self, code, sanc, curr):
		self.code = code
		self.sanc = sanc
		self.addl = sanc - curr
		self.vacancy = sanc - curr
		self.curr = curr
		self.orig = curr
		self.lowestcpi = 900

	def remove(self):
		self.curr = self.curr - 1
		if (self.curr < math.ceil(3.0*self.sanc/4) ):
			self.curr = self.curr + 1
			return False
		else:
			self.curr = self.curr + 1
			return True

	def add(self):
		self.curr = self.curr + 1
		if (self.sanc%10 >= 5):
			flag = 1
		else:
			flag=0
		if (self.curr > self.sanc + (self.sanc/10) + flag):
			self.curr = self.curr -1
			return False
		else:
			self.curr = self.curr -1
			return True

students=[]

def check(stu, branch):
	index1 = students.index(stu)
	stu.lower = -1

	i = index1 - 1
	while i>=0:				# Check karna hai ????????
		if branch in students[i].pref:
			stu.lower = students[i].cpi
			break
		i = i-1

	if stu.lower == -1:
		return True
	else:
		return False


def checkEqual(stu, branch):
	if br[branch].lowestcpi <= stu.cpi:
		return True
	else:
		return False


def compare(stu, stud):
	if (stu.cpi != stud.cpi):
		return cmp(stud.cpi, stu.cpi)
	else:
		return cmp( 1.0*(br[dict2[stud.curr]].curr-1)/(br[dict2[stud.curr]].orig) , 1.0*(br[dict2[stu.curr]].curr-1)/(br[dict2[stu.curr]].orig))

dict2 = {}
# Take branch data from CSV
branches =[]

# Branch data
with open('branches.csv', 'r') as csvf:
	data = csv.reader(csvf, delimiter=',', quotechar='|')
	i = 0
	for row in data:
		dict[row[0]] = i
		dict2[i] = row[0]
		branches.append(Branch(row[0], int(row[1]), int(row[2])))
		br[row[0]] = Branch(i, int(row[1]), int(row[2]))
		i =i+1

csvf.close()
#----------------------

size_prev = 0

studentsdone = []

# Take data from DB -----------
with open('e_input.csv', 'r') as csvf:
	data = csv.reader(csvf, delimiter=',', quotechar='|')
	for row in data:
		pref=[]
		for i in range(5, len(row)):
			if row[i] == '':
				continue
			else:
				pref.append(row[i])
		temp = Student(row[0], float(row[3]), dict[row[2]], pref, row[1], row[4])
		if ((temp.cat == "GE" or temp.cat == "OBC") and temp.cpi >=8.00):
			students.append(temp)
		elif ((temp.cat == "SC" or temp.cat == "ST") and temp.cpi >=7.00):
			students.append(temp)
		else:
			temp.curr = "Ineligible"
			studentsdone.append(temp)


csvf.close()
#-----------------------

is_Stable = False

def getcpi(s):
	return s.cpi

#one time sort suffices
students.sort(compare)
#for stu in students:
#	print stu.name, stu.cpi, stu.curr
#students = sorted(students, key = getcpi, reverse = True)
size_prev = len(students)
count = 0

while is_Stable == False:
	is_Stable = True
	index = 0
	count = count +	1
	while index < len(students):
		stu = students[index]
		stu.prev = stu.curr
		if (br[stu.pref[0]].add() == True):
			if (stu.cpi >=9.00):
				if (check(stu, stu.pref[0]) == True):
					br[stu.pref[0]].curr += 1
					students[index].update(dict[stu.pref[0]])
					studentsdone.append(students[index])
					br[dict2[stu.prev]].curr -= 1
					del (students[index])
					continue			# continue to the next index
			else:		## CPI < 9 here
				if br[dict2[stu.curr]].remove() == False:
					i = len (studentsdone)-1
					flag = 0
					#if stu.name == 'rws':
					#	print "Yahan par hai"
					while i>=0:
						if ((studentsdone[i].cpi == stu.cpi) and ((studentsdone[i].orig == stu.orig) or (studentsdone[i].curr == dict[stu.pref[0]]))):
							br[stu.pref[0]].curr +=1
							students[index].update(dict[stu.pref[0]])
							br[dict2[stu.prev]].curr -=1
							studentsdone.append(students[index])
							del students[index]
							#print "NOW"
							index = index-1
							flag = 1
							break
						i = i-1

					if (flag ==0):
						j = index-1
						while (j >= 0):
							if ((students[j].cpi == stu.cpi) and (((students[j].orig == stu.orig) and (students[j].orig != students[j].curr)) or (students[j].curr == dict[stu.pref[0]]))):
								br[stu.pref[0]].curr +=1
								students[index].update(dict[stu.pref[0]])
								br[dict2[stu.prev]].curr -=1
								studentsdone.append(students[index])
								del students[index]
								#print "THEN"
								index = index-1
								flag = 1
								break
							j = j-1

					index = index +1
					#print "POST"
					#if stu.name == 'rws':
					#	print "sdfgh"
					continue	# Cannot be removed with cpi < 9 so nothing to do, iterate to next person
				else:
					if check(stu, stu.pref[0]) == False:		# Can go to the next preference
						#goto next pref
						a=0
					else:
						br[stu.pref[0]].curr += 1
						#print stu.cpi, stu.name, dict2[stu.orig], stu.pref[0]

						#if stu.name == 'rws':
						#	print "DEFG", br[stu.pref[0]].curr, br[dict2[stu.curr]].curr, stu.prev, stu.curr

						#if stu.name == 'mfg':
						#	print "ABC", br[stu.pref[0]].curr, br[dict2[stu.curr]].curr, stu.prev, stu.curr 
						students[index].update(dict[stu.pref[0]])
						br[dict2[stu.prev]].curr -= 1
						studentsdone.append(students[index])
						del students[index]					## He got this branch even if his cpi was < 9 and so he is done.
						continue

		if (br[stu.pref[0]].add() == False and checkEqual(stu, stu.pref[0]) == True):		## Accounts for Tanmay and Ritwick
			br[stu.pref[0]].curr += 1
			students[index].update(dict[stu.pref[0]])
			br[dict2[stu.prev]].curr -= 1
			studentsdone.append(students[index])  
			del students[index]
			#if stu.name == 'rws':
			#	print "Yahan par hai 1"
			continue

		for i in stu.pref[1:]:
			#print stu.name, i, br[i].curr
			if (br[i].add() == True):
				#print "True ke andar"
				if (stu.cpi >= 9.00):
					if (check(stu, i) == True):
						students[index].update(dict[i]);
						br[i].curr +=1
						br[dict2[stu.prev]].curr -= 1
						break
					else:
						continue
				else:				## CPI less than 9 ... Now depends on what the source branch strength is
					if br[dict2[stu.curr]].remove() == False:
						m = len (studentsdone)-1
						flag = 0
						while m>=0:
							if ((studentsdone[m].cpi == stu.cpi) and ((studentsdone[m].orig == stu.orig) or (studentsdone[m].curr == dict[i]))):
								br[i].curr +=1
								students[index].update(dict[i])
								br[dict2[stu.prev]].curr -=1
								#studentsdone.append(students[index])
								#del students[index]
								#print "HERE"
								flag = 1
								break
							m = m-1

						if (flag ==0):
							j = index-1
							while (j >= 0):
								if ((students[j].cpi == stu.cpi) and (((students[j].orig == stu.orig) and (students[j].orig != students[j].curr)) or (studentsdone[j].curr == dict[i]))):
									br[i].curr +=1
									students[index].update(dict[i])
									br[dict2[stu.prev]].curr -=1
									#print "THERE"
									#studentsdone.append(students[index])
									#del students[index]
									#index = index-1
									flag = 1
									break
								j = j-1
						#print "ALPHA"
						break 			## No scpe, branch remains same
					else:
						if check(stu, i) == False:
							continue
						else:
							students[index].update(dict[i])
							#if stu.name == 'mfg':
							#	print "DEF", br[i].curr, br[dict2[stu.prev]].curr, stu.prev, stu.curr 
							#if stu.name == 'rws':
							#	print stu.curr, stu.prev
							br[i].curr += 1
							br[dict2[stu.prev]].curr -= 1
							break

			if (br[i].add() == False and checkEqual(stu, i) == True):
				br[i].curr += 1
				br[dict2[stu.prev]].curr -=1
				students[index].update(dict[i])
				break

		index = index + 1

	#print "Iteration Complete ----------------------"

	students.sort(compare)

	if len(students) != size_prev:
		size_prev = len(students)
		#print "Length:::", size_prev
		is_Stable = False

	else:
		for stu in students:
			if (stu.curr != stu.prev):
				is_Stable = False
				#print "h"
				break

	'''print "New -----------------------------------"
	for stu in students:
		print stu.roll, stu.name, stu.cpi, stu.prev, stu.curr
	
	for stu in studentsdone:
		print stu.roll, stu.name, stu.cpi, stu.prev, stu.curr

	print "Finish --------------------------------"
	
	for i in range(0, len(br)):
		print br[dict2[i]].code, br[dict2[i]].curr
	
	print "Start----------------------------------"'''

#print count

out_csv = csv.writer(open('stats12.csv', 'w'), dialect='excel')
out2 = csv.writer(open('allotted12.csv', 'w'), dialect='excel')

for i in range(0, len(br)):
	br[dict2[i]].lowestcpi = 12

#print "Final Strengths of branches is: -----------------"
for stu in students:
	if (stu.orig !=stu.curr):
		br[dict2[stu.curr]].lowestcpi = min(br[dict2[stu.curr]].lowestcpi, stu.cpi);

for stu in studentsdone:
	if (stu.orig !=stu.curr and stu.curr!='Ineligible'):
		br[dict2[stu.curr]].lowestcpi = min(br[dict2[stu.curr]].lowestcpi, stu.cpi);
	

out_csv.writerow(['Program', 'Cutoff', 'Sanctioned Strength', 'Original Strength', 'Final Strength'])

for i in range(0, len(br)):
	if (br[dict2[i]].lowestcpi == 12):
		br[dict2[i]].lowestcpi = 'NA'
	row = []
	row.append(dict2[i])
	row.append(br[dict2[i]].lowestcpi)
	row.append(br[dict2[i]].sanc)
	row.append(br[dict2[i]].orig)
	row.append(br[dict2[i]].curr)
	out_csv.writerow(row)


#print "Final Branches Allotted are--------------------"

for stu in students:
	if stu.orig != stu.curr:
		row = []
		row.append(stu.roll)
		row.append(stu.name)
		#row.append(stu.cpi)
		row.append(dict2[stu.orig])
		row.append(dict2[stu.curr])
		out2.writerow(row)
	else:
		row=[]
		row.append(stu.roll)
		row.append(stu.name)
		#row.append(stu.cpi)
		row.append(dict2[stu.orig])
		row.append("Branch Unchanged")
		out2.writerow(row)

for stu in studentsdone:
	if stu.curr == "Ineligible":
		row=[]
		row.append(stu.roll)
		row.append(stu.name)
		#row.append(stu.cpi)
		row.append(dict2[stu.orig])
		row.append("Ineligible")
		out2.writerow(row) 
	else:
		row = []
		row.append(stu.roll)
		row.append(stu.name)
		#row.append(stu.cpi)
		row.append(dict2[stu.orig])
		row.append(dict2[stu.curr])
		out2.writerow(row)				
