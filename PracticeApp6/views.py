from django.shortcuts import render

from PracticeApp6.models import CarData1

# Create your views here.

def home_fun(request):
    return render(request, 'index.html')



def read_fun(request):
    c2 = CarData1()
    c2.c_name = request.POST['txtCarName']
    c2.c_company = request.POST['txtCarCompany']
    c2.c_model = request.POST['txtCarModel']
    c2.c_price = int(request.POST['txtCarPrice'])
    c2.c_fueltype = request.POST['slFuelType']
    c2.save()
    return render(request, 'index.html', {'Msg': 'Data Enter Successfully'})


def disp_fun(request):
    data = CarData1.objects.all()
    return render(request, 'CarData.html', {'Data': data})
