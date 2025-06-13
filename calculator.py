import config

def calculate_total_average(english, c_language, python):
    total = english + c_language + python
    average = round(total / 3, 2)
    return total, average

def calculate_grade(average):
    for grade, min_score in config.GRADE_CRITERIA.items():
        if average >= min_score:
            return grade
    return 'F'
    
def validate_score(score):
    return 0 <= score <= 100

def calculate_rank(students_list):
    sorted_students = sorted(students_list, key=lambda x: x['total'], reverse=True)
    for rank, student in enumerate(sorted_students, 1):
        student['rank'] = rank
    return students_list
        
