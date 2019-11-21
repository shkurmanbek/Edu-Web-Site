from django.contrib import admin
from .models import Teacher, Student, Comment
# Register your models here.


class SubjectInline(admin.StackedInline):
    model = Comment
    extra = 2


class TeacherAdmin(admin.ModelAdmin):
    class Meta:
        db_table = "teachers"

    fields = ['teacher_name', 'teacher_surname', 'subject_name', 'mark_date']
    list_filter = ['mark_date']


class StudentAdmin(admin.ModelAdmin):
    class Meta:
        db_table = "students"

    fields = ['student_name', 'student_surname', 'teacher_mark']
    inlines = [SubjectInline]


admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Comment)
