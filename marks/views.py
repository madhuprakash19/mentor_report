from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from marks.models import student

@login_required()
def home(request):
    temp = list(student.objects.all())
    print(temp)
    return render(request,'index.html',{'temp':temp})
