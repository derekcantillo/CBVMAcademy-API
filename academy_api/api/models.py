from django.db import models

# Create your models here.



class Course(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    level=models.IntegerField()

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['name']

    def __str__(self):
        return self.name

class Group(models.Model):
    name=models.CharField( max_length=50)
    direction=models.CharField( max_length=100)
    nameleader=models.CharField( max_length=50)
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = ['name']

    def __str__(self):
        return self.name
  

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    bday=models.DateField( auto_now=False, auto_now_add=False)
    numdoc=models.CharField(max_length=50)
    blood=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    id_group=models.ForeignKey(Group, on_delete=models.CASCADE, default="")

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        ordering = ['name']

    def __str__(self):
        return self.name

class Promo(models.Model):
    name=models.CharField(max_length=50)
    id_teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, default="")
    id_course=models.ForeignKey(Course, on_delete=models.CASCADE, default="")
   
    class Meta:
        verbose_name = "Promo"
        verbose_name_plural = "Promos"
        ordering = ['name']

    def __str__(self):
        return  str(self.id_course) + self.name 

class Student(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    bday=models.DateField( auto_now=False, auto_now_add=False)
    numdoc=models.CharField(max_length=50)
    blood=models.CharField(max_length=50)
    email=models.EmailField( max_length=254)
    id_group=models.ForeignKey(Group, on_delete=models.CASCADE, default="")
    promo=models.ManyToManyField(Promo, verbose_name="Promo", blank=True, through="PromoStudent")
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['name']

    def __str__(self):
        return self.name
class PromoStudent(models.Model):
    promo=models.ForeignKey(Promo, verbose_name="Promo", on_delete=models.CASCADE, blank=True, null=True)
    student=models.ForeignKey(Student, verbose_name="Student", on_delete=models.CASCADE, blank=True, null=True)
    state=models.CharField(max_length=50)
    

    class Meta:
        verbose_name = "PromoStudent"
        verbose_name_plural = "PromoStudents"

    def __str__(self):
        return str(self.student) + '-'+ str(self.promo) + '-' + self.state

