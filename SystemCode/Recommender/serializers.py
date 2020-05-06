from rest_framework import serializers
from .models import Student
from .models import University_Course

# Not needed for now
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'preferred_country', 'ielts_score']

class University_CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = University_Course
        fields = ['id','name','country','population_size','age','status','academic_reputation_score','academic_reputation_rank','employer_reputation_score','employer_reputation_rank','faculty_student_score','faculty_student_rank','citation_score','citation_rank','international_faculty_score','international_faculty_rank','international_student_score','international_student_rank','overall_score','city','region','cost_of_living_index','international_student_percentage','field_of_study','subject','program_name','min_IELTS','min_TOEFL','min_GPA','campus_setting','offer_work_study_program','average_tuition_fee','offer_airport_pickup','acceptance_rate']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = University_Course
        fields = ['country']

def StudentDeSerializer(data):
    return Student(
        region = data['region'] if 'region' in data else '',
        country = data['country'] if 'country' in data else '',
        academic_reputation_rank  = data['academic_reputation_rank'] if 'academic_reputation_rank' in data else '',
        employer_reputation_rank  = data['employer_reputation_rank'] if 'employer_reputation_rank' in data else '',
        faculty_student_rank  = data['faculty_student_rank'] if 'faculty_student_rank' in data else '',
        international_faculty_rank  = data['international_faculty_rank'] if 'international_faculty_rank' in data else '',
        international_student_rank  = data['international_student_rank'] if 'international_student_rank' in data else '',
        citation_rank  = data['citation_rank'] if 'citation_rank' in data else '',
        ielts  = data['ielts'] if 'ielts' in data else '',
        toefl  = data['toefl'] if 'toefl' in data else '',
        work_study  = data['work_study'] if 'work_study' in data else '',
        min_tution_fee  = data['min_tution_fee'] if 'min_tution_fee' in data else '',
        max_tution_fee  = data['max_tution_fee'] if 'max_tution_fee' in data else '',
        international_student_percentage  = data['international_student_percentage'] if 'international_student_percentage' in data else '',
        cost_index  = data['cost_index'] if 'cost_index' in data else '',
        math  = data['math'] if 'math' in data else '',
        chinese  = data['chinese'] if 'chinese' in data else '',
        english  = data['english'] if 'english' in data else '',
        physics  = data['physics'] if 'physics' in data else '',
        chemistry  = data['chemistry'] if 'chemistry' in data else '',
        biology  = data['biology'] if 'biology' in data else '',
        history  = data['history'] if 'history' in data else '',
        geogrophy  = data['geogrophy'] if 'geogrophy' in data else '',
        politics  = data['politics'] if 'politics' in data else '',
        art  = data['art'] if 'art' in data else ''
        )