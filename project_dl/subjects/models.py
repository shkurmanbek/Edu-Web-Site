from django.db import models

# Create your models here.

class Student(models.Model):
    class Meta:
        db_table = "students"
    student_name = models.CharField(max_length=200)
    student_surname = models.CharField(max_length=200)
    teacher_mark = models.IntegerField(default=0)

class Teacher(models.Model):
    class Meta:
        db_table = "teachers"
    teacher_name = models.CharField(max_length=200)
    teacher_surname = models.CharField(max_length=200)
    subject_name = models.CharField(max_length=200)
    mark_date = models.DateTimeField()

class Comment(models.Model):
    class Meta:
        db_table = 'comments_s'
    comment_text = models.TextField()
    comment_subject = models.ForeignKey(Student, on_delete=models.CASCADE)