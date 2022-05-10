from django.contrib import admin
from . import  models

admin.site.register(models.student)
admin.site.register(models.teacher)
admin.site.register(models.department)
admin.site.register(models.designation)
admin.site.register(models.student_hostel)

