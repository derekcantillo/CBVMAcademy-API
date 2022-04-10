from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.

class StudentView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            students=list(Student.objects.filter(id=id).values())
            if len(students)>0:
                student=students[0]
                data={'message' : "Success", 'student':student}
            else:
                data={'message' : "Students not found"}
            return JsonResponse(data)

    def post(self, request):

        jload = json.loads(request.body)
        Student.objects.create(
            name=jload['name'], 
            phone=jload['phone'],
            bday=jload['bday'],
            numdoc=jload['numdoc'],
            blood=jload['blood'],
            email=jload['email'],
            id_group=jload['id_group'],
            promo=jload['promo']

        )
        data={'message': "Student created"}
        
        return JsonResponse(data)

    def put(self, request, id):
        pass
    def delete(self, request, id):
        pass

