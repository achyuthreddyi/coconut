from django.shortcuts import render ,redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

 


# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
            user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('user created')
            return render(request,'success.html')
        else :
            return HttpResponse('sorry user not created')
       



    else:
        return render(request,'register.html')

    return redirect('/')
    # return render(request,'register.html')
    # return HttpResponse('hello') 

def select(request):

    if request.method=="GET":

        return render(request,'select.html')

    else:
        temperature = request.POST['first_name']
        humidity = request.POST['last_name']
        rainfall = request.POST['username']

        
        return render(request,'selectres.html')
        
   
    
    




def login(request):
    

    if request.method=='GET':
        return render(request,'login.html')
        

    else:
        
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('success.html')
            # return redirect("/")
        else:
            # message.info(request,'invalid credentials')
            return redirect('success.html')


    
    


    