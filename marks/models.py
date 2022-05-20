from django.db import models
from django.contrib.auth.models import User

class department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    HOD = models.ForeignKey(User,related_name='HOD',on_delete = models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.id)+" "+str(self.name)


class student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    adm_no = models.IntegerField(blank=True,null=True)
    usn = models.CharField(max_length=15,blank=True,null=True)
    year_of_joining = models.IntegerField(blank=True,null=True)
    year_of_passout = models.IntegerField(blank=True,null=True)
    dept_id = models.ForeignKey(department,on_delete = models.CASCADE,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=20,blank=True,null=True)
    father_name = models.CharField(max_length=50,blank=True,null=True)
    mother_name = models.CharField(max_length=50,blank=True,null=True)
    guardian_name = models.CharField(max_length=50,blank=True,null=True)
    student_phone_number = models.IntegerField(blank=True,null=True)
    father_phone_number = models.IntegerField(blank=True,null=True)
    mother_phone_number = models.IntegerField(blank=True,null=True)
    guardian_phone_number = models.IntegerField(blank=True,null=True)
    student_mail = models.EmailField(max_length=50,blank=True,null=True)
    parent_mail = models.EmailField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=50,blank=True,null=True)
    class_ten_percentage = models.CharField(max_length=15,blank=True,null=True)
    class_twelve_percentage = models.CharField(max_length=15,blank=True,null=True)
    medium_of_study = models.CharField(max_length=50,blank=True,null=True)


    def __str__(self):
        return str(self.name)

class designation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)+" "+str(self.name)

class teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    dept_id = models.ForeignKey(department,related_name='dept_id',on_delete = models.CASCADE,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)
    phone_number = models.IntegerField(blank=True,null=True)
    dob = models.DateField(max_length=10,blank=True,null=True)
    gender = models.CharField(max_length=20,blank=True,null=True)
    designation_id = models.ForeignKey(designation,related_name='designation_id',on_delete = models.CASCADE,blank=True,null=True)
    year_of_joining = models.IntegerField(blank=True,null=True)
    address =  models.CharField(max_length=50,blank=True,null=True)

class student_hostel(models.Model):
    student_adm_no = models.ForeignKey(User,on_delete = models.CASCADE,blank=True,null=True)
    student_year = models.IntegerField(blank=True,null=True)
    hostel_name = models.CharField(max_length=50,blank=True,null=True)
    room_no = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return str(self.student_adm_no)



class role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)+" "+str(self.name)

class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    role_id = models.ForeignKey(role,on_delete = models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.user)

class placement(models.Model):
    user =models.ForeignKey(User,on_delete = models.CASCADE,blank=True,null=True)
    company = models.CharField(max_length=50,blank=True,null=True)
    ctc = models.CharField(max_length=25,blank=True,null=True)

    def __str__(self):
        return str(self.user)+" "+ str(self.company)

class competitive_exams(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,blank=True,null=True)
    exam = models.CharField(max_length=50, blank=True, null=True)
    date_of_exam = models.DateField()
    grade = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.user)+" "+ str(self.exam)


class subject(models.Model):
    name = models.CharField(max_length=50,blank=True,null=True)
    code = models.CharField(max_length=10,blank=True,null=True)
    dept_id = models.ForeignKey(department,on_delete = models.CASCADE,blank=True,null=True)
    description = models.CharField(max_length=50,blank=True,null=True)
    credit = models.IntegerField(blank=True,null=True,default=3)


    def __str__(self):
        return str(self.name)+" "+str(self.code)

class mentor_list(models.Model):
    student = models.ForeignKey(User,related_name='mstudent',on_delete = models.CASCADE,blank=True,null=True)
    faculty = models.ForeignKey(User,related_name='mfaculty',on_delete = models.CASCADE,blank=True,null=True)
    sem = models.IntegerField(blank=True,null=True)
    section =  models.CharField(max_length=5,blank=True,null=True)
    ay = models.CharField(max_length=15,blank=True,null=True)

    def __str__(self):
        return str(self.student)+" "+ str(self.faculty)

class mentor_data(models.Model):
    student_meta = models.ForeignKey(mentor_list,on_delete = models.CASCADE,blank=True,null=True)
    subject = models.ForeignKey(subject,on_delete = models.CASCADE,blank=True,null=True)
    mse1_marks =  models.CharField(max_length=10,blank=True,null=True,default=0)
    mse2_marks =  models.CharField(max_length=10,blank=True,null=True,default=0)
    mse3_marks =  models.CharField(max_length=10,blank=True,null=True,default=0)
    mse1_attndence =  models.CharField(max_length=10,blank=True,null=True,default=0)
    mse2_attndence =  models.CharField(max_length=10,blank=True,null=True,default=0)
    mse3_attndence =  models.CharField(max_length=10,blank=True,null=True,default=0)
    la1 =  models.CharField(max_length=10,blank=True,null=True,default=0)
    la2 =  models.CharField(max_length=10,blank=True,null=True,default=0)
    final_cie =  models.CharField(max_length=10,blank=True,null=True,default=0)
    final_attendence =  models.CharField(max_length=10,blank=True,null=True,default=0)

    def __str__(self):
        return str(self.student_meta)+" "+ str(self.subject)
