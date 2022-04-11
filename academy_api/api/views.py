from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Teacher, Group
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
        else:
            students=list(Student.objects.values())
            if len(students)>0:
                data={'message': "Success", 'students': students}
            else:
                data={'message': "Students no found"}
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
            id_group=jload['id_group']

        )
        data={'message': "Student created"}
        
        return JsonResponse(data)

    def put(self, request, id):
        jload = json.loads(request.body)
        students=list(Student.objects.filter(id=id).values())

        if len (students)>0:
            student = Student.objects.get(id=id)
            student.name=jload['name']
            student.phone=jload['phone']
            student.bday=jload['bday']
            student.numdoc=jload['numdoc']
            student.blood=jload['blood']
            student.email=jload['email']
            student.id_group_id=jload['id_group_id']
            student.save()
            data = {'message': "Student updated"}
        else:
            data={'message': "Student not found"}
        
        return JsonResponse(data)

    def delete(self, request, id):
        students = list(Student.objects.filter(id=id).values())
        if len(students)>0:
            Student.objects.filter(id=id).delete()
        else:
            data={'message': "Student not found"}
        return JsonResponse(data)

class TeacherView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
      if(id>0):
          teachers=list(Teacher.objects.filter(id=id).values())
          if len(teachers)>0:
              teacher=teachers[0]
              data={'message': "Success" , 'teacher':teacher}
          else:
              data={'message': "Group not found"}
          return JsonResponse(data)
      else:
          teachers=list(Teacher.objects.values())
          if len(teachers)>0:
            
              data={'message': "Success" , 'teachers':teachers}
          else:
              data={'message': "Groups not found"}
          return JsonResponse(data)

    def post(self, request):

        jload = json.loads(request.body)
        
        Teacher.objects.create(
            name=jload['name'], 
            phone=jload['phone'],
            bday=jload['bday'],
            numdoc=jload['numdoc'],
            blood=jload['blood'],
            email=jload['email'],
            id_group=jload['id_group']

        )
        data={'message': "Teacher created"}
        
        return JsonResponse(data)
    
    def put(self, request, id):
        jload = json.loads(request.body)
        teachers = list(Teacher.objects.filter(id=id).values())
        if len(teachers)>0:
            teacher = Teacher.objects.get(id=id)
            teacher.name=jload['name']
            teacher.phone=jload['phone']
            teacher.bday=jload['bday']
            teacher.numdoc=jload['numdoc']
            teacher.blood=jload['blood']
            teacher.email=jload['email']
            teacher.id_group_id=jload['id_group_id']
            teacher.save()
            data = {'message': "Teacher updated"}
        else:
            data={'message': "Teacher not found"}
        
        return JsonResponse(data)
    
    def delete(self, request, id):
        teachers = list(Teacher.objects.filter(id=id).values())
        if len(teachers)>0:
            Teacher.objects.filter(id=id).delete()
        else:
            data={'message': "Teacher deleted"}
        return JsonResponse(data)

class GroupView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
      if(id>0):
          groups=list(Group.objects.filter(id=id).values())
          if len(groups)>0:
              group=groups[0]
              data={'message': "Success" , 'group':group}
          else:
              data={'message': "Group not found"}
          return JsonResponse(data)
      else:
          groups=list(Group.objects.values())
          if len(groups)>0:
            
              data={'message': "Success" , 'groups':groups}
          else:
              data={'message': "Groups not found"}
          return JsonResponse(data)

    def post(self, request):
        jload=json.loads(request.body)

        Group.objects.create(
            name=jload['name'], 
            direction=jload['direction'],
            nameleader=jload['nameleader']
        )
        data={'message': "Group created"}
        return JsonResponse(data)

    def put(self, request, id):
        jload = json.loads(request.body)
        groups=list(Group.objects.filter(id=id).values())
        if len(groups)>0:
            group=Group.objects.get(id=id)
            group.name=jload['name'], 
            group.direction=jload['direction'],
            group.nameleader=jload['nameleader']
            group.save()
            data={'message': "Group updated"}
        else:
            data={'message': "Group not found"}
        return JsonResponse(data)
    
    def delete(self, request, id):
        groups = list(Group.objects.filter(id=id).values())
        if len(groups)>0:
            Group.objects.filter(id=id).delete()
        else:
            data={'message': "Group not found"}    

            