from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from .forms import RegisterForm
from .models import Register
from django.contrib import messages
from customer.models import Customer
# Create your views here.
def new_transation(request):
    c = Register.objects.all().order_by('-id')[:5]
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, '1 Transation Added Successfully !')
        return redirect('new_transation')
    d ={
        'form':form,
        'c': c,
    }


    return render(request,'register/new_transation.html',d)

def show_transations(request):
    total_credit =0.00
    total_cash =0.00

    cus = Customer.objects.all()




    c = Register.objects.all()



    cr = Register.objects.filter(type='credit')
    dr = Register.objects.filter(type='cash')

    for i in cr:
        total_credit = total_credit + float(i.amount)

    for i in dr:
        total_cash = total_cash + float(i.amount)

    context ={
        'c':c,
        'total_credit':total_credit,
        'total_cash':total_cash,
        'remaining':total_cash-total_credit,
    }

    return render(request,'register/all_transations.html',context)


def details_customer(request,id):

    cus_detail = Register.objects.filter(type__iexact='credit')
    print(cus_detail)
    context ={
        'cus_detail':cus_detail,
    }
    return render(request, 'register/customer_details.html')
