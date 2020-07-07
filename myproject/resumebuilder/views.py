from django.shortcuts import render
from . models import Usertable,Resumetable

def login(request):
    if(request.method=="POST"):
        email=request.POST['email']
        key=request.POST['pass']
        print(email)
        print(key)
        address=Usertable.objects.filter(email=email,password=key)
        if not address:
            return render(request,'index.html', {'message':'Login failed'})
        else:
            return render(request,'profile.html', {'message':'Login successful'})
    else:
        return render(request, 'index.html')

def main(request):
    return render(request,'index.html')

def add_user(request):
    if(request.method=="POST"):
        name=request.POST['uname']
        email=request.POST['uemail']
        password=request.POST['upass']
        cpass=request.POST['cpass']
        auth=Usertable.objects.filter(email=email, password=password)
        if not auth:
            if(password==cpass):
                ob = Usertable()
                ob.name = name
                ob.email = email
                ob.password = password
                ob.save()
                return render(request,'reg.html',{'message':'Account created successfully'})
            else:
                return render(request,'reg.html',{'message':'Please check password entered'})
        else:
            return render(request,'reg.html',{'message':'Mail address alreday taken'})

def profile(request):
    if(request.method=="POST"):
        email = request.POST['pemail']
        ob = Resumetable.objects.get(email=email)
        if not ob:
            ob = Resumetable()
            ob.name=request.POST['pname']
            ob.email=request.POST['pemail']
            ob.phone=request.POST['phone']
            ob.address=request.POST['address']

            ob.degree=request.POST['pd1']
            ob.puc=request.POST['pd2']
            ob.school=request.POST['pd3']

            ob.institute_1=request.POST['pu1']
            ob.institute_2=request.POST['pu2']
            ob.institute_3=request.POST['pu3']

            ob.marks_1=request.POST['ps1']
            ob.marks_2=request.POST['ps2']
            ob.marks_3=request.POST['ps3']

            ob.experience=request.POST['experience']
            ob.skills=request.POST['skills']
            ob.project=request.POST['project']
            ob.objective=request.POST['objective']
            ob.hobbies=request.POST['hobbies']
            ob.save()
            ob = Resumetable.objects.filter(email=email)

            return render(request,'resume.html',{'details':ob})
        else:
            ob.name=request.POST['pname']
            ob.email=request.POST['pemail']
            ob.phone=request.POST['phone']
            ob.address=request.POST['address']

            ob.degree=request.POST['pd1']
            ob.puc=request.POST['pd2']
            ob.school=request.POST['pd3']

            ob.institute_1=request.POST['pu1']
            ob.institute_2=request.POST['pu2']
            ob.institute_3=request.POST['pu3']

            ob.marks_1=request.POST['ps1']
            ob.marks_2=request.POST['ps2']
            ob.marks_3=request.POST['ps3']

            ob.experience=request.POST['experience']
            ob.skills=request.POST['skills']
            ob.project=request.POST['project']
            ob.objective=request.POST['objective']
            ob.hobbies=request.POST['hobbies']
            ob.save()
            ob = Resumetable.objects.filter(email=email)

            return render(request,'resume.html',{'details':ob})

    else:
        return render(request,'profile.html')

    
def resume(request):
    return render(request,'resume.html')