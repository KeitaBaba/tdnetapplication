from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from.models import Tekijikaiji,Customer
from .forms import CustomerForm
import csv
from django.contrib.auth.decorators import login_required

class TopView(generic.TemplateView):
    template_name = 'tdnet/top.html'


def index(request):
    tekijikaiji=Tekijikaiji.objects.all()
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
    code=request.POST.get('code')
    csv_file_name=request.POST.get('customer')
    customer_address=request.POST.get('customer_address')


    if Customer.objects.filter(customer_address = customer_address):
        return render(request, "tdnet/error.html", {"error":"このユーザーは登録されています"})
    
    if customer_address=="" :
        with open(csv_file_name+".csv", 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([code])
        
        return render(request, 'tdnet/create.html')
        
    elif code=="" and form.is_valid():
            Customer.objects.create(**form.cleaned_data)
            return render(request, 'tdnet/create.html')
        

    else:
        with open(csv_file_name+".csv", 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([code])

        if form.is_valid():
            Customer.objects.create(**form.cleaned_data)
            return render(request, 'tdnet/create.html')  
