from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, default="unset")
    preferred_country =  models.CharField(max_length=50, default="unset")
    ielts_score = models.FloatField(max_length=50, default=0.0)


class University_Course(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50, default="unknown")
    country = models.CharField(max_length=20, default="unknown")
    population_size = models.CharField(max_length=20, default="unknown")
    age = models.PositiveSmallIntegerField(default = 0)
    status = models.CharField(max_length=20, default="unknown")
    academic_reputation_score = models.FloatField(max_length=20, default=0.0)
    academic_reputation_rank = models.PositiveSmallIntegerField(default = 0)
    employer_reputation_score = models.FloatField(max_length=20, default=0.0)
    employer_reputation_rank = models.PositiveSmallIntegerField(default = 0)
    faculty_student_score = models.FloatField(max_length=20, default=0.0)
    faculty_student_rank = models.PositiveSmallIntegerField(default = 0)
    citation_score = models.FloatField(max_length=20, default=0.0)
    citation_rank = models.PositiveSmallIntegerField(default = 0)
    international_faculty_score	= models.FloatField(max_length=20, default=0.0)
    international_faculty_rank = models.PositiveSmallIntegerField(default = 0)
    international_student_score	= models.FloatField(max_length=20, default=0.0)
    international_student_rank = models.PositiveSmallIntegerField(default = 0)
    overall_score = models.FloatField(max_length=20, default=0.0)
    city = models.CharField(max_length=20, default="unknown")
    region = models.CharField(max_length=20, default="unknown")
    cost_of_living_index = models.FloatField(max_length=20, default=0.0)
    international_student_percentage = models.FloatField(max_length=20, default=0.0)
    field_of_study = models.CharField(max_length=20, default="unknown")
    subject = models.CharField(max_length=50, default="unknown")
    program_name = models.CharField(max_length=20, default="unknown")
    min_IELTS = models.FloatField(max_length=20, default=0.0)	
    min_TOEFL = models.FloatField(max_length=20, default=0.0)
    min_GPA	= models.CharField(max_length=20, default="unknown")
    campus_setting = models.CharField(max_length=20, default="unknown")
    offer_work_study_program = models.BooleanField(default=False)
    average_tuition_fee = models.PositiveIntegerField(default = 0)
    offer_airport_pickup = models.BooleanField(default=False)
    acceptance_rate = models.FloatField(max_length=20, default=0.0)


class Country(models.Model):
    name = models.CharField(max_length=50)

