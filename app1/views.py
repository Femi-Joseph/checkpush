from django.shortcuts import render,redirect
from app1.models import*
from app1.utils import render_to_pdf
from io import BytesIO,StringIO
from django.core.files import File


# Create your views here.
def index(request):
    return render(request,'index.html')
    
def base(request):
    return render(request,'base.html')

def client_login(request):
    flag=0
    if request.method=='GET':
        return render(request,'client_login.html')
    else:
        print('hi iam here')
        email=request.POST.get('email')
        pwd=request.POST.get('password')
        print(email,pwd)
        error_message=None
        try:
            print("In try")
            client_obj=Client.objects.get(email=email)
            print("client=",client_obj)

        except:
            error_message="client does not exisit"
            return render(request,'client_login.html',{'error':error_message})
        data={'client_obj':client_obj}

        print("data=",data)

        if client_obj and client_obj.status==1:
            if (pwd==client_obj.pwd):
                flag=1

            if flag:
                request.session['id']=client_obj.id
                request.session['name']=client_obj.clientname
                return render(request,"client_home.html",data)
            else:
                error_message='email or password invalid !'
                return render(request,"client_login.html",{'error':error_message})

        else:
            if client_obj.status==0:
                error_message="admin permission requierd"
            else:
                error_message='email or password invalid !'
        return render(request,"client_login.html",{'error':error_message})
    return render(request,"client_login.html",{'error':error_message})

        
    return render(request,'client_login.html')

def client_signup(request):
    return render(request,'client_signup.html')

def client_register(request):
    if request.method=='POST':
        client_name=request.POST.get('client_name')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        password=request.POST.get('password2')
        aadhar_number=request.POST.get('aadhar_number')
        contact_number=request.POST.get('contact_number')
        photo=request.FILES['photo']
        print(client_name,email)
        client_obj=Client(clientname=client_name,email=email,pwd=password,aadhar=aadhar_number,contact=contact_number,photo=photo)
        client_obj.save()
        return redirect('client_admin_msg')
        
    return render(request,'client_signup.html')

def client_home(request):
    return render(request,'client_home.html')

def client_data(request):
    if request.method=="GET":
        '''obj1=Client.objects.get(id=request.session['id'])
        obj=Clientdata.objects.filter(client=Client(request.session['id']))
        if obj:
            obj=clientdata.objects.filter(client=Client(request.session['id'])).order_by('-id')[0]
            print (obj)
            return render(request,'client_data.html',{'obj':obj,'obj1':obj1})
        else:
            return render(request,'client_data.html',{'obj1':obj1})'''
        return render(request,'client_data.html')
    if request.method=="POST":
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        adress=request.POST.get('adress')
        district=request.POST.get('district')
        contry=request.POST.get('contry')
        pincode=request.POST.get('pincode')
        education=request.POST.get('education')
        print('dob=',dob)
        obj=Clientdata(dob=dob,gender=gender,adress=adress,district=district,contry=contry,pincode=pincode,education=education,client=Client(request.session['id']))
        obj.save()
        obj1=Client.objects.filter(id=request.session['id'])
        
        global pdf
        pdf=render_to_pdf(obj.id,'client_profilecard.html',{'obj':obj,'obj1':obj1})
        document=Clientdocument(client=Clientdata(obj.id))
        global filename
        filename="doc%s.pdf"%(obj.id)
        document.pdfdata.save(filename,File(BytesIO(pdf.content)))
        document.save()
        return render(request,'client_profilecard.html',{'obj':obj,'obj1':obj1})
        


    return render(request,'client_data.html')

def client_admin_msg(request):
    return render (request,'client_admin_msg.html')

def client_datacollect(request):
    return render (request,'client_datacollect.html')

def client_profilecard(request):
    return render (request,'client_profilecard.html')


    


