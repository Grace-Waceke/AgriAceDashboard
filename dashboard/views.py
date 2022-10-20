# from multiprocessing import context
# from django.shortcuts import render

# # Create your views here.
# def dashboard_with_pivot(request):
#     return render(request, 'dashboard_with_pivot.html', {})

# def index(request):
#     return render (request, "home/home.html")


# def card(request):
#     context={}
#     return render (request, "card.html", context)

from django.http import JsonResponse
from django.shortcuts import redirect, render
from dashboard.forms import FarmerForm
from dashboard.models import Farmer
from django.core import serializers

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})

# def pivot_data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize('json', dataset)
#     return JsonResponse(data, safe=False)


def index(request):
    return render(request, 'index.html')


def farmer_Form(request):
    if request.method=="POST":
        form=FarmerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("farmerslist")
        else:
            print(form.errors)
    else:
        form=FarmerForm()   
    return render(request,"farmers_Form.html",{"form":form}) 

def farmers_list(request):
    farmers=Farmer.objects.all()
    return render(request,"farmers_list.html",{"farmers":farmers})    

 




