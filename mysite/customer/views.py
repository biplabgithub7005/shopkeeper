from django.shortcuts import render,redirect,HttpResponse
from .forms import CustomerForm,ExampleForm
from .models import Customer
from register.models import Register
from django.contrib import messages
from django.contrib.auth import logout

from django.contrib.auth import logout
# Create your views here.

def customer_signup(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('signup')

        messages.add_message(request, messages.INFO, 'Customer Added Successfully !')
    d ={
        'form':form
    }


    return render(request,'customer/signup.html',d)

def show_customer(request):
    c = Customer.objects.all()
    t = Register.objects.all()

    context ={
        'c':c,
        't':t,
    }

    return render(request,'customer/customers.html',context)

def update_customer(request,id):
    customer = Customer.objects.get(id=id)



    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('all_customers')

    d = {
        'form': form
    }
    return render(request,'customer/signup.html',d)


def delete_customer(request,id):
    customer =Customer.objects.get(id=id)
    if request.method =='POST':

        customer.delete()
        return redirect('all_customers')
    return render(request,'customer/confirm.html')
    # return HttpResponse("Data delete ho gya")


def customer_dashboard(request):
    mycus=''
    if request.session['mycustomer']:
        mycus =request.session['mycustomer']
    else:
        redirect('cus_login')

    c = Customer.objects.count()


    context = {
        'c': c,
        'mycus':mycus
    }

    return render(request,'dashbord.html',context)


def matltiplae(request):




    form = ExampleForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    return render(request,'malti.html',{'form':form})
#
# def customer_login(request):
#     form =CustomerLogin(request.POST or None)
#     if form.is_valid():
#         email =form.cleaned_data.get('email')
#         password =form.cleaned_data.get('password')
#         # print(email,password)
#         user_auth =Customer.objects.filter(email=email,password=password)
#         if user_auth.exists():
#             request.session['mycustsomer']=email
#
#             return redirect('dashboard')
#         else:
#             messages.warning(request, 'Your Email and Password Not Valid')
#     d = {
#         'form': form
#     }
#     return render(request,'customer/login.html',d)
#
#
# def customer_logout(request):
#     logout(request)
#     return redirect('login')


def customer_login(request):


    if request.method=='POST':
        email =request.POST['email']
        password =request.POST['password']

        user_auth=Customer.objects.filter(email=email,password=password)
        if user_auth.exists():
            request.session['mycustomer']=email
            return redirect('dashboard')
        else:
            messages.warning(request, 'Your Email id or Password Not Correct')

        # print(email,password)


    return render(request,'customer/customer_login.html')

def customer_logout(request):
    logout(request)
    return redirect('cus_login')