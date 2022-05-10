# Generated by Django 3.2.5 on 2022-05-10 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('HOD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HOD', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('year_of_joining', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('dept_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dept_id', to='marks.department')),
                ('designation_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='designation_id', to='marks.designation')),
            ],
        ),
        migrations.CreateModel(
            name='student_hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_year', models.IntegerField(blank=True, null=True)),
                ('hostel_name', models.CharField(blank=True, max_length=50, null=True)),
                ('room_no', models.IntegerField(blank=True, null=True)),
                ('student_adm_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('adm_no', models.IntegerField(blank=True, null=True)),
                ('usn', models.CharField(blank=True, max_length=15, null=True)),
                ('year_of_joining', models.IntegerField(blank=True, null=True)),
                ('year_of_passout', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('guardian_name', models.CharField(blank=True, max_length=50, null=True)),
                ('student_phone_number', models.IntegerField(blank=True, null=True)),
                ('father_phone_number', models.IntegerField(blank=True, null=True)),
                ('mother_phone_number', models.IntegerField(blank=True, null=True)),
                ('guardian_phone_number', models.IntegerField(blank=True, null=True)),
                ('student_mail', models.EmailField(blank=True, max_length=50, null=True)),
                ('parent_mail', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('class_ten_percentage', models.CharField(blank=True, max_length=15, null=True)),
                ('class_twelve_percentage', models.CharField(blank=True, max_length=15, null=True)),
                ('medium_of_study', models.CharField(blank=True, max_length=50, null=True)),
                ('dept_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='marks.department')),
            ],
        ),
    ]