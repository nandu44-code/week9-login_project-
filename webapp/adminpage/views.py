from django.shortcuts import get_object_or_404, render,redirect
from .models import Customers
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)

def Adminpage_login(request):
    if 'admin_name' in request.session:
        return redirect('admin_page')
    
    if request.method=="POST":
        user_name=request.POST.get('username')
        user_password=request.POST.get('password')

        user=authenticate(request,username=user_name,password=user_password)

        if user:
            if user.is_superuser:
                request.session['admin_name']=user_name
                login(request,user)
           
                return redirect('admin_page')
            else:
                messages.error(request,"sorry,Invalid credentials") 
                return redirect('admin_login')
        else:
            messages.error(request,"lsorry,login with admin credentials") 
            return redirect('admin_login')

    return render(request,'adminlogin.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)   
@login_required(login_url='admin_login')
def Adminpage(request):
    if 'q' in request.GET:
        q=request.GET['q']
        multiple_q=Q(Q(user_name__icontains=q) | Q(email__icontains=q))
        customer=Customers.objects.filter(multiple_q)

        context={
            "customers":customer,
        }

    else:
        customer=Customers.objects.all()

        context={
            "customers":customer,
        }

    return render(request,'adminDash.html',context)
def add(request):
    if 'admin_name' in request.session:
        if request.method=='POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            c_password=request.POST.get('confirm_password')
            

            exist_username = User.objects.filter(username=name)
            if exist_username.exists():
                    messages.error(request, 'username already taken')
                    return redirect('admin_page')
            if password == c_password:
                    my_user = User.objects.create_user(username=name, password=password, email=email)
                    my_user.save()
                    customer=Customers( user_name=name,email=email)
                    customer.save()
                    return redirect("admin_page")
            else:
                    messages.error(request, 'password not matching try again..')
                    return redirect('admin_page')
        
    else:
        return redirect('admin_login')
    
    return render(request, 'adminDash.html')

             
        
            
    # return render(request,'adminDash.html') 

def Edit(request):
    customer=Customers.objects.all()

    context={
            "customers":customer,
        }
    return render(request,'adminDash.html') 


  

def Update(request,id):

    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')

        customer=Customers(
          id=id,
          user_name=name,
          email=email

        )
        customer.save()

        return redirect('admin_page')
@cache_control(no_cache=True, no_store=True)
@login_required(login_url='admin_login') 
def User_Delete(request,id):
    if 'admin_name' in request.session:
        user=user = User.objects.filter(id=id)
        customer=get_object_or_404(Customers,id=id)
        user.delete()
        customer.delete()
        return redirect('admin_page')
    else:     
         return redirect('admin_login')
    
# @cache_control(no_cache=True, no_store=True)
@login_required(login_url='admin_login')
def admin_logout(request):
    if 'admin_name' in request.session:
        
           logout(request)
    return redirect('admin_login')
        
    
