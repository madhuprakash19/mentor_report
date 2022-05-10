from django.contrib import admin
from . import  models

admin.site.register(models.student)
admin.site.register(models.teacher)
admin.site.register(models.department)
admin.site.register(models.designation)
admin.site.register(models.student_hostel)
admin.site.register(models.user_profile)
admin.site.register(models.role)
admin.site.register(models.placement)
admin.site.register(models.competitive_exams)
admin.site.register(models.subject)
admin.site.register(models.mentor_list)
admin.site.register(models.mentor_data)


