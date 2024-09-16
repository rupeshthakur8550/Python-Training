from django.shortcuts import render

def all_chai(request):
    return render(request, 'app_1/chai_all_type.html')
