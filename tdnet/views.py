from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from.models import Tekijikaiji,Customer,Code
from .forms import CustomerForm,CodeForm
import csv
from datetime import datetime,timedelta
import datetime
from django.contrib.auth.decorators import login_required

class TopView(generic.TemplateView):
    template_name = 'tdnet/top.html'


def index(request):
    td = timedelta(days=-30)
    d = datetime.date.today()
    date=td+d
    one_month_ago=date.strftime('%Y%m%d')
    
    tekijikaiji=Tekijikaiji.objects.all().filter(disclosure_date__gt=one_month_ago).order_by('-disclosure_date')
    keyword = request.GET.get('keyword')
    if keyword:
       tekijikaiji = tekijikaiji.filter(
                Q(company_title__icontains=keyword)| Q(company_name__icontains=keyword)| Q(code__icontains=keyword)
       )
    
    params={     
        'tekijikaiji':tekijikaiji,
        }
    return render(request, 'tdnet/index.html', params)

@login_required
def new(request):
    form = CustomerForm(request.POST or None) 
    params = {
        'form' : form,
    }
    return render(request, 'tdnet/new.html', params)

@login_required
def customer_models(request):
    form = CustomerForm(request.POST or None) 
    form2 = CodeForm(request.POST or None) 
    code=request.POST.get('code')
    csv_file_name=request.POST.get('customer')
    customer_address=request.POST.get('customer_address')


    if Customer.objects.filter(customer_address = customer_address):
        return render(request, "tdnet/error.html", {"error":"このユーザーは登録されています"})
    
    if customer_address=="" and  form2.is_valid():
        Code.objects.create(**form2.cleaned_data)
        return render(request, 'tdnet/create.html')

    if customer_address=="" and code=="":
        return render(request, 'tdnet/error.html',{"error":"銘柄コードを入力してください"})

    if code=="" and  form.is_valid():
        Customer.objects.create(**form.cleaned_data)
        return render(request, 'tdnet/create.html')
    
    if form.is_valid() and form2.is_valid():
            Customer.objects.create(**form.cleaned_data)
            Code.objects.create(**form2.cleaned_data)
            return render(request, 'tdnet/create.html')  
