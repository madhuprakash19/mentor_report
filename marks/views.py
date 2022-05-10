from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from marks.models import student, user_profile

def faculty_status(user):
    teacher = user_profile.objects.get(user=user)
    if teacher.role_id.id == 2:
        return True
    else:
        return False

@login_required()
def home(request):
    temp = list(student.objects.all())
    print(temp)
    return render(request,'index.html',{'temp':temp})
