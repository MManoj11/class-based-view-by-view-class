from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
def fbv_string(request):
    return HttpResponse('this is function based view for displaying a string')

#using cbv for string
class CBV_string(View):
    def get(self,request):
        return HttpResponse('this is class based view for displaying a string')

#using fbv in html
def fbv_html(request):
    return render(request,'fbv_html.html')

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
