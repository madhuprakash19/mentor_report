from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from marks.models import mentor_list
import openpyxl


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


def mapping(request):
    if "GET" == request.method:
        return render(request, 'mapping.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_file)
        worksheet = wb["Book1"]
        print(worksheet)
        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        for i in range (1,len(excel_data)):
            usn = excel_data[i][0]
            mentor = excel_data[i][1]
            sem_ = excel_data[i][2]
            section_ = excel_data[i][3]
            ay_ = excel_data[i][4]

            try:
                student=User.objects.create_user(usn, password=usn)
                t = User.objects.create_user(mentor, password=mentor)
                student.save()
                print(usn+" created")
            except:
                print(usn+" already Exists")

            student_ = User.objects.get(username=usn)
            teacher_ = User.objects.get(username=mentor)

            try:
                temp =  mentor_list.objects.get(student=student_,ay=ay_)
                temp.faculty = teacher_
                temp.save()
            except:
                temp = mentor_list(student=student_,faculty=teacher_,sem=sem_,section=section_,ay=ay_)
                temp.save()



        return render(request, 'mapping.html', {"excel_data":excel_data})
