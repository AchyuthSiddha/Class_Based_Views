from typing import Any, Dict
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.generic import View,TemplateView
from app.forms import *
#Function Base View

def FBV_string(request):
    return HttpResponse("this is FBV string:")


# Class Based View

class CBV_string(View):
    def get(self,request):
        return HttpResponse("this is CBV string")
    


# Function Based Using Html Page

def FBV_html(request):
    return render(request,'FBV_html.html')

# Class Based using Html Page

class CBV_html(View):
    def get(self,request):
        return render(request,'CBV_html.html')
    
# Function based using Form

def FBV_Form(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFOD=TopicForm(request.POST)
        if TFOD.is_valid():
            TFOD.save()
            return HttpResponse("data inserted sucessfully:")

    return render(request,'FBV_Form.html',d)

# class CBV_Form(View):
#     def get(self,request):
#         TFO=TopicForm()
#         d={'TFO':TFO}
#         return render(request,'CBV_Form.html',d)
#     def post(self,request):
#         TFOD=TopicForm(request.POST)
#         if TFOD.is_valid():
#             TFOD.save()
    
#         return HttpResponse("data inserted sucessfullY:")
class CBV_Form(View):
    def get(self, request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'CBV_Form.html',d)

    def post(self, request):
        TFOD=TopicForm(request.POST)
        if TFOD.is_valid():
            TFOD.save()
        return HttpResponse('data is inserted')

# class Dummy(TemplateView):
#     template_name='Dummy.html'

class CBV_Context(TemplateView):
    template_name='CBV_Context.html'

    def get_context_data(self, **kwargs):
        ECO=super().get_context_data(**kwargs)
        ECO['name']='Achyuth'
        ECO['age']=24
        ECO['email']='achyuthsiddha43@gmail.com'
        return ECO
