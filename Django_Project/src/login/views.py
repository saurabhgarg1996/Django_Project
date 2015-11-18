from django.shortcuts import render, render_to_response
from login.forms import *
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.views import login
from login.models import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
import shutil
import os 
from django.core.files import File
from django.contrib import messages
from input.models import *
from Branch_change import settings
from django.core.servers.basehttp import FileWrapper
import mimetypes    
from django.utils.encoding import smart_str
import csv
import random, sys
import math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
@csrf_protect
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})
 
def register_success_view(request):
    return render(request,'success.html',{})
 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home')
 
def empty_view(request):
    return HttpResponseRedirect('/home')

def home_view(request):
    if request.user.is_authenticated():
        if request.user.username == 'admin':
            return HttpResponseRedirect('/admin1')
        else:
            return HttpResponseRedirect('/fillform')
    else:
        return login(request)
def admin_view(request):
    if request.user.is_authenticated() and request.user.username == 'admin':
        return render(request,'admin1.html',{'documents' : Document.objects.all()})
    else:
        return login(request)
def upload(request):
    # Handle file upload
    if request.user.is_authenticated() and request.user.username == 'admin':
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile = request.FILES['docfile'])
                newdoc.save()
                tpCast = str(request.FILES['docfile'])
                if tpCast == 'Students_data.csv' :
                    Test.objects.all().delete()
                    FILE_DIR = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","media","Students_data.csv")
                    with open(FILE_DIR) as csvf:
                        row = csv.reader(csvf, delimiter=',', quotechar='|')
                        for myrow in row:
                            myrow[1]=float(myrow[1].strip(' "'))            
                            tmp=Test(myrow[0],myrow[1])
                            tmp.save()
                            # Redirect to the document list after POST
                            
                return render(request,'admin1.html',{'documents' : Document.objects.all()})
        else:
            form = DocumentForm() # A empty, unbound form
        # Load documents for the list page
        documents = Document.objects.all()

        # Render list page with the documents and the form
        return render_to_response(
            'upload.html',
            {'documents': documents, 'form': form},
            context_instance=RequestContext(request)
        )
    else:
        return login(request)

def delete(request):
    if request.user.is_authenticated() and request.user.username == 'admin':
        if os.path.exists(os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","media"))== True :
            Document.objects.all().delete();
            shutil.rmtree(os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","media"))
            return render(request,'admin1.html',{})
        else :
           # messages.add_message(request, messages.INFO, 'No Files to delete')
            return render(request,'admin1.html',{})
    else:
        return login(request)
def data_view(request): 
    if request.user.is_authenticated() and request.user.username == 'admin':   
        data = Student.objects.all()
        FILE_DIR= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","Applied_Students.csv")
        with open(FILE_DIR, 'wb') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            # write your header first
            for obj in Student.objects.all():
                row = []
                name = ""
                name = obj.first_name+" "+obj.last_name
                row.append(obj.roll_number)
                row.append(name)
                row.append(obj.present_branch)
                row.append(obj.cpi)
                row.append(obj.category)
                if(obj.preference_1!="None"):
                    row.append(obj.preference_1)
                if(obj.preference_2!="None"):
                    row.append(obj.preference_2)
                if(obj.preference_3!="None"):
                    row.append(obj.preference_3)
                if(obj.preference_4!="None"):
                    row.append(obj.preference_4)
                if(obj.preference_5!="None"):
                    row.append(obj.preference_5)
                if(obj.preference_6!="None"):
                    row.append(obj.preference_6)
                if(obj.preference_7!="None"):
                    row.append(obj.preference_7)
                if(obj.preference_8!="None"):
                    row.append(obj.preference_8)
                if(obj.preference_9!="None"):
                    row.append(obj.preference_9)
                if(obj.preference_10!="None"):
                    row.append(obj.preference_10)
                if(obj.preference_11!="None"):
                    row.append(obj.preference_11)
                if(obj.preference_12!="None"):
                    row.append(obj.preference_12)
                if(obj.preference_13!="None"):
                    row.append(obj.preference_13)
                if(obj.preference_14!="None"):
                    row.append(obj.preference_14)
                if(obj.preference_15!="None"):
                    row.append(obj.preference_15)
                if(obj.preference_16!="None"):
                    row.append(obj.preference_16)
                print(row)
                writer.writerow(row)

        return render(request,'table_view.html',{'data' : data })
    else:
        return login(request)
def download(request,file_name):
    if request.user.is_authenticated() and request.user.username == 'admin':   
        file_path = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root")+'/'+ file_name
        file_wrapper = FileWrapper(file(file_path,'rb'))
        file_mimetype = mimetypes.guess_type(file_path)
        response = HttpResponse(file_wrapper, content_type=file_mimetype )
        response['X-Sendfile'] = file_path
        response['Content-Length'] = os.stat(file_path).st_size
        response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name) 
        return response
    else:
        return login(request)

def roll_to_cpi(request): 
    Test.objects.all().delete()
    for i in range(0, 100):
        b = random.random()
        a=round(b, 2)*10
        tmp=Test(150000000+i,a)
        tmp.save()
    return render(request,'roll_to_cpi.html',{})
    # FILE_DIR = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","Roll_to_CPI.csv")
    # out_csv = csv.writer(open(FILE_DIR,'w'), dialect='excel')
    # for i in range(0, 10000000):
    #     row=[]
    #     row.append(150000000+i)
    #     b = random.random()
    #     a=round(b, 2)*10
    #     row.append(a)
    #     out_csv.writerow(row)
    #     Test.objects.all().delete()
                #     FILE_DIR = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","media","Roll_to_CPI.csv")
                #     with open(FILE_DIR) as csvf:
                #         row = csv.reader(csvf, delimiter=',', quotechar='|')
                #         for myrow in row:
                #             myrow[1]=float(myrow[1].strip(' "'))            
                #             tmp=Test(myrow[0],myrow[1])
                #             tmp.save()
                #             # Redirect to the document list after POST
def onwhat(request):
    return render(request,'algorithm.html',{})
def code_1(request):
    if request.user.is_authenticated() and request.user.username == 'admin':   
        # if os.path.exists(os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","Applied_Students.csv"))== True :
        #     a=1
        # else:
        FILE_DIR= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","Applied_Students.csv")
        with open(FILE_DIR, 'wb') as csvfile:
            writer = csv.writer(csvfile,delimiter=',')
            # write your header first
            for obj in Student.objects.all():
                row = []
                name = ""
                name = obj.first_name+" "+obj.last_name
                row.append(obj.roll_number)
                row.append(name)
                row.append(obj.present_branch)
                row.append(obj.cpi)
                row.append(obj.category)
                if(obj.preference_1!="None"):
                    row.append(obj.preference_1)
                if(obj.preference_2!="None"):
                    row.append(obj.preference_2)
                if(obj.preference_3!="None"):
                    row.append(obj.preference_3)
                if(obj.preference_4!="None"):
                    row.append(obj.preference_4)
                if(obj.preference_5!="None"):
                    row.append(obj.preference_5)
                if(obj.preference_6!="None"):
                    row.append(obj.preference_6)
                if(obj.preference_7!="None"):
                    row.append(obj.preference_7)
                if(obj.preference_8!="None"):
                    row.append(obj.preference_8)
                if(obj.preference_9!="None"):
                    row.append(obj.preference_9)
                if(obj.preference_10!="None"):
                    row.append(obj.preference_10)
                if(obj.preference_11!="None"):
                    row.append(obj.preference_11)
                if(obj.preference_12!="None"):
                    row.append(obj.preference_12)
                if(obj.preference_13!="None"):
                    row.append(obj.preference_13)
                if(obj.preference_14!="None"):
                    row.append(obj.preference_14)
                if(obj.preference_15!="None"):
                    row.append(obj.preference_15)
                if(obj.preference_16!="None"):
                    row.append(obj.preference_16)
                print(row)
                writer.writerow(row)
        dict = {}           #Name vs. code dictionary
        br = {}             # Name vs branch object dictionary

        #---------------  Base class : Student (Stores - CPI, Current Branch Number, Preference List, Roll Number) -----------#
        class student:

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
            while i>=0:             # Check karna hai ????????
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
        FILE_DIR= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","Applied_Students.csv") 
        # Branch data
        FILE_DIR1= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","media","input_programmes.csv")    
                
        # Branch data
        with open(FILE_DIR1, 'r') as csvf:
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
        with open(FILE_DIR, 'r') as csvf:
            data = csv.reader(csvf, delimiter=',', quotechar='|')
            for row in data:
                pref=[]
                for i in range(5, len(row)):
                    if row[i] == '':
                        continue
                    else:
                        pref.append(row[i])
                if len(pref) == 0:
                    continue
                temp = student(row[0], float(row[3]), dict[row[2]], pref, row[1], row[4])
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
        #   print stu.name, stu.cpi, stu.curr
        #students = sorted(students, key = getcpi, reverse = True)
        size_prev = len(students)
        count = 0

        while is_Stable == False:
            is_Stable = True
            index = 0
            count = count + 1
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
                            continue            # continue to the next index
                    else:       ## CPI < 9 here
                        if br[dict2[stu.curr]].remove() == False:
                            i = len (studentsdone)-1
                            flag = 0
                            #if stu.name == 'rws':
                            #   print "Yahan par hai"
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
                            #   print "sdfgh"
                            continue    # Cannot be removed with cpi < 9 so nothing to do, iterate to next person
                        else:
                            if check(stu, stu.pref[0]) == False:        # Can go to the next preference
                                #goto next pref
                                a=0
                            else:
                                br[stu.pref[0]].curr += 1
                                #print stu.cpi, stu.name, dict2[stu.orig], stu.pref[0]

                                #if stu.name == 'rws':
                                #   print "DEFG", br[stu.pref[0]].curr, br[dict2[stu.curr]].curr, stu.prev, stu.curr

                                #if stu.name == 'mfg':
                                #   print "ABC", br[stu.pref[0]].curr, br[dict2[stu.curr]].curr, stu.prev, stu.curr 
                                students[index].update(dict[stu.pref[0]])
                                br[dict2[stu.prev]].curr -= 1
                                studentsdone.append(students[index])
                                del students[index]                 ## He got this branch even if his cpi was < 9 and so he is done.
                                continue

                if (br[stu.pref[0]].add() == False and checkEqual(stu, stu.pref[0]) == True):       ## Accounts for Tanmay and Ritwick
                    br[stu.pref[0]].curr += 1
                    students[index].update(dict[stu.pref[0]])
                    br[dict2[stu.prev]].curr -= 1
                    studentsdone.append(students[index])  
                    del students[index]
                    #if stu.name == 'rws':
                    #   print "Yahan par hai 1"
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
                        else:               ## CPI less than 9 ... Now depends on what the source branch strength is
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
                                break           ## No scpe, branch remains same
                            else:
                                if check(stu, i) == False:
                                    continue
                                else:
                                    students[index].update(dict[i])
                                    #if stu.name == 'mfg':
                                    #   print "DEF", br[i].curr, br[dict2[stu.prev]].curr, stu.prev, stu.curr 
                                    #if stu.name == 'rws':
                                    #   print stu.curr, stu.prev
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

        FILE_DIR= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","output_stats_applied.csv")
        FILE_DIR1= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","allotment_applied.csv")
        f1 = open(FILE_DIR, 'w')
        f2 = open(FILE_DIR1, 'w')
        out_csv = csv.writer(f1, dialect='excel')
        out2 = csv.writer(f2, dialect='excel')

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
        
        f1.close()
        f2.close()
        Allotted.objects.all().delete()
        count=0
        with open(FILE_DIR1,'r') as csvf:
            row = csv.reader(csvf, delimiter=',', quotechar='|') 
            for myrow in row:
                count +=1
                tmp=Allotted(str(count),myrow[0],myrow[1],myrow[2],myrow[3])
                tmp.save()

        Stats.objects.all().delete()
        with open(FILE_DIR,'r') as csvf:
            row = csv.reader(csvf, delimiter=',', quotechar='|')
            count = 0
            for myrow in row:
                if count == 0:
                    a=1
                    count = count + 1
                else :
                    myrow[2]=int(myrow[2].strip(' "'))            
                    myrow[3]=int(myrow[3].strip(' "'))            
                    myrow[4]=int(myrow[4].strip(' "'))            
                    tmp=Stats(myrow[0],myrow[1],myrow[2],myrow[3],myrow[4])
                    tmp.save()
        return render(request,'allotment1.html',{'Allotted' : Allotted.objects.all(),'Stats' : Stats.objects.all()})
    else:
        return login(request)
def code_2(request):
    if request.user.is_authenticated() and request.user.username == 'admin':   
        # if os.path.exists(os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","Applied_Students.csv"))== True :
        #     a=1
        # else:
        dict = {}           #Name vs. code dictionary
        br = {}             # Name vs branch object dictionary

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
            while i>=0:             # Check karna hai ????????
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
        FILE_DIR= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","media","input_options.csv") 
        # Branch data
        FILE_DIR1= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","media","input_programmes.csv")    
                        
        # Branch data
        with open(FILE_DIR1, 'r') as csvf:
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
        with open(FILE_DIR, 'r') as csvf:
            data = csv.reader(csvf, delimiter=',', quotechar='|')
            for row in data:
                pref=[]
                for i in range(5, len(row)):
                    if row[i] == '':
                        continue
                    else:
                        pref.append(row[i])
                if len(pref) == 0:
                    continue
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
        #   print stu.name, stu.cpi, stu.curr
        #students = sorted(students, key = getcpi, reverse = True)
        size_prev = len(students)
        count = 0

        while is_Stable == False:
            is_Stable = True
            index = 0
            count = count + 1
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
                            continue            # continue to the next index
                    else:       ## CPI < 9 here
                        if br[dict2[stu.curr]].remove() == False:
                            i = len (studentsdone)-1
                            flag = 0
                            #if stu.name == 'rws':
                            #   print "Yahan par hai"
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
                            #   print "sdfgh"
                            continue    # Cannot be removed with cpi < 9 so nothing to do, iterate to next person
                        else:
                            if check(stu, stu.pref[0]) == False:        # Can go to the next preference
                                #goto next pref
                                a=0
                            else:
                                br[stu.pref[0]].curr += 1
                                #print stu.cpi, stu.name, dict2[stu.orig], stu.pref[0]

                                #if stu.name == 'rws':
                                #   print "DEFG", br[stu.pref[0]].curr, br[dict2[stu.curr]].curr, stu.prev, stu.curr

                                #if stu.name == 'mfg':
                                #   print "ABC", br[stu.pref[0]].curr, br[dict2[stu.curr]].curr, stu.prev, stu.curr 
                                students[index].update(dict[stu.pref[0]])
                                br[dict2[stu.prev]].curr -= 1
                                studentsdone.append(students[index])
                                del students[index]                 ## He got this branch even if his cpi was < 9 and so he is done.
                                continue

                if (br[stu.pref[0]].add() == False and checkEqual(stu, stu.pref[0]) == True):       ## Accounts for Tanmay and Ritwick
                    br[stu.pref[0]].curr += 1
                    students[index].update(dict[stu.pref[0]])
                    br[dict2[stu.prev]].curr -= 1
                    studentsdone.append(students[index])  
                    del students[index]
                    #if stu.name == 'rws':
                    #   print "Yahan par hai 1"
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
                        else:               ## CPI less than 9 ... Now depends on what the source branch strength is
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
                                break           ## No scpe, branch remains same
                            else:
                                if check(stu, i) == False:
                                    continue
                                else:
                                    students[index].update(dict[i])
                                    #if stu.name == 'mfg':
                                    #   print "DEF", br[i].curr, br[dict2[stu.prev]].curr, stu.prev, stu.curr 
                                    #if stu.name == 'rws':
                                    #   print stu.curr, stu.prev
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
        FILE_DIR= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","output_stats.csv")
        FILE_DIR1= os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root","allotment.csv")        
        f1 = open(FILE_DIR, 'w')
        f2 = open(FILE_DIR1, 'w')
        out_csv = csv.writer(f1, dialect='excel')
        out2 = csv.writer(f2, dialect='excel')

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
        f1.close()
        f2.close()
        Allotted.objects.all().delete()
        count=0
        with open(FILE_DIR1,'r') as csvf:
            row = csv.reader(csvf, delimiter=',', quotechar='|') 
            for myrow in row:
                count +=1
                tmp=Allotted(str(count),myrow[0],myrow[1],myrow[2],myrow[3])
                tmp.save()

        Stats.objects.all().delete()
        with open(FILE_DIR,'r') as csvf:
            row = csv.reader(csvf, delimiter=',', quotechar='|')
            count = 0
            for myrow in row:
                if count == 0:
                    a=1
                    count = count + 1
                else :
                    myrow[2]=int(myrow[2].strip(' "'))            
                    myrow[3]=int(myrow[3].strip(' "'))            
                    myrow[4]=int(myrow[4].strip(' "'))            
                    tmp=Stats(myrow[0],myrow[1],myrow[2],myrow[3],myrow[4])
                    tmp.save()
        return render(request,'allotment.html',{'Allotted' : Allotted.objects.all(),'Stats' : Stats.objects.all()})
    else:
        return login(request)