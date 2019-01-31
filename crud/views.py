from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View
from crud.mixins import HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
# Functions based views:
def emp_data_view(request):
    emp_data = {
        "eno": 100,
        "ename": "rishabh",
        "esal": 1000,
        "eadd": "Delhi"
    }
   # resp = 'Employee Number:{}Employee Name:{}:Employee Salary:{}:Employee Address:{}'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eadd'])
    resp = json.dumps(emp_data)
    return HttpResponse(resp,content_type='application/json')

class CrudClass(View):
    def get(self,request,*args,**kwargs):
        emp_data = {
            "eno": 100,
            "ename": "rishabh",
            "esal": 1000,
            "eadd": "Delhi"
        }
        return JsonResponse(emp_data)

@method_decorator(csrf_exempt,name='dispatch')
class CrudTest(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        resp = json.dumps({"msg" : "This is from get"})
        return self.render_to_http_response(resp)
    def post(self,request,*args,**kwargs):
        resp = json.dumps({"msg" : "This is from post"})
        return self.render_to_http_response(resp)
    def put(self,request,*args,**kwargs):
        resp = json.dumps({"msg" : "This is from put"})
        return self.render_to_http_response(resp)
    def delete(self,request,*args,**kwargs):
        resp = json.dumps({"msg" : "This is from delete"})
        return self.render_to_http_response(resp)


