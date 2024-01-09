from django.contrib import admin
from .models import Student, Teacher, Freshman, Transferee


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Freshman)
admin.site.register(Transferee)
