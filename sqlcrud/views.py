from django.shortcuts import render
from django.views.generic import View
from crud.mixins import HttpResponseMixin
from sqlcrud.mixins import FilterFields
import json
from sqlcrud.models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.serializers import serialize
from utils.utils import is_valid
from sqlcrud.forms import EmployeeForm

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class SQLCRUD(HttpResponseMixin,FilterFields,View):
    def get(self,request,*args,**kwargs):
        emp = Employee.objects.all()
        final_data = self.filtered(emp)
        return self.render_to_http_response(final_data)
    def post(self,request,*args,**kwargs):
        data = request.body.decode('utf-8')
        valid_json = is_valid(data)
        if not valid_json:
            json_data = json.dumps({"msg" : "Please give valid data"})
            return self.render_to_http_response(json_data,status = 412)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({"msg": " Created Successfully"})
            return self.render_to_http_response(json_data, status=201)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=412)


@method_decorator(csrf_exempt,name='dispatch')
class SQLCRUDID(HttpResponseMixin,FilterFields,View):
    def get_obejct_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return self.render_to_http_response(json.dumps({"msg" : "requested resource does not exist"}),status = 404)
        else :
            final_data = self.filtered([emp,])
        return self.render_to_http_response(final_data)
    def put(self,request,id,*args,**kwargs):
        emp = self.get_obejct_by_id(id)
        if emp is None:
            return self.render_to_http_response(json.dumps({"msg" : "requested resource does not exist"}),status = 404)
        data = request.body.decode('utf-8')
        valid_json = is_valid(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({"msg" : "Please Provide Valid json"}),status = 417)
        provided_data = json.loads(data)
        original_data = {
            "eno" : emp.eno,
            "ename" : emp.ename,
            "esal" : emp.esal,
            "eaddr":emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({"msg" : "Updated Successfully"}),status = 202)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=417)
    def delete(self,request,id,*args,**kwargs):
        emp = self.get_obejct_by_id(id)
        if emp is None:
            return self.render_to_http_response(json.dumps({"msg" : "requested resource does not exist"}),status = 404)
        status,deleted_item =emp.delete() # delete returns a tuple (status,deleted item)
        if status == 1:
            return self.render_to_http_response(json.dumps({"msg" : "Deleted Successfully"}),status = 202)
        return self.render_to_http_response(json.dumps({"msg": "Not able to Delete "}), status=202)













