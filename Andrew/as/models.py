from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.teacher

class Student(models.Model):
    name = models.CharField(max_length=50, null=True)
    student_number = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lrn = models.IntegerField()
    age = models.IntegerField()
    grade_level = models.CharField(max_length=50, null=True)

    YEAR_IN_SCHOOL_COURSE_STRAND = [
        ("HM", "HOSPITALITY MANAGEMENT"),
        ("CS", "COMPUTER SCIENCE"),
        ("IT", "ICT"),
        ("AB", "ABM"),

    ]
    Course_and_Strand = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_COURSE_STRAND)

    # def __str__(self):
    #     return self.name


class Freshman(models.Model):
    school_graduated = models.CharField(max_length=100, null=True)
    year_grad = models.CharField(max_length=100, null=True)



class Transferee(models.Model):
    student_name = models.ForeignKey(Student, default=1, on_delete=models.CASCADE)
    grade_level = models.IntegerField()
    previous_school = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.student_name