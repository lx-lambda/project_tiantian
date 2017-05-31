from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'df_user/index.html')
    # return HttpResponse('heeeeeee')