from django.contrib import admin
from .models import Course, Group, Teacher, Promo, Student, PromoStudent
# Register your models here.

admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Teacher)
admin.site.register(Promo)
admin.site.register(Student)
admin.site.register(PromoStudent)