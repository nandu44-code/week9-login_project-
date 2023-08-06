from django import urls
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.cache import cache_control
# from adminpage import urls
# Create your views here.


def signup(request):
        if 'username_new' in request.session:
            return redirect ('home_page')
        
    
        if request.method=='POST':
            user_name=request.POST.get('username_new')
            email_adress=request.POST.get('email')
            pass1=request.POST.get('password')
            pass2=request.POST.get('confirm_password')  

            username_checking=User.objects.filter(username=user_name)
            email_checking=User.objects.filter(email=email_adress)

            if  username_checking.exists():
                messages.error(request,"username is already taken") 
                return redirect('user_signup')
            if  email_checking.exists():
                messages.error(request,"email is already taken") 
                return redirect('user_signup')
            elif pass2==pass1:
                my_user=User.objects.create_user(user_name,email_adress,pass1)
                my_user.save()
                messages.success(request,"account created successfully") 
                return redirect('user_login')
            else:
                messages.error(request,"password you re entered is incorrect") 
                return redirect('user_signup')
    

        return render(request,'signup.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
         return render(request,'home.html')
    else:
        return redirect('user_login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):
    if 'username' in request.session:
        return redirect('home_page')
    if 'admin_name' in request.session:
        return redirect('admin_page')

    if request.method=="POST":
        user_name=request.POST.get('username')
        user_password=request.POST.get('password')
        user=authenticate(request,username=user_name,password=user_password)
       
        if user is not None:
            login(request,user)
            request.session['username']=user_name
            return redirect('home_page')
        else:
            messages.error(request,"username or password is incorrect") 
            return redirect('user_login')
            # return HttpResponse("username or password is incorrect")    
             
    return render(request,'login.html')

def logout_user(request):

    if 'username' in request.session:

        logout(request)

    return redirect('user_login')

def admin_login_page(request):


    return redirect('admin_login')