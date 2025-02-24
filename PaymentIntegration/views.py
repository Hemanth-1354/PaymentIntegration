from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')


def failed(request):
    return render(request, 'failed.html')