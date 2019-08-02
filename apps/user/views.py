from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views.generic import View


class indexView(View):
    def get(self,request):
        return render(request,'index.html')

#
# def index(request):
#     return HttpResponse('djangoProject Start')