from database import db_manager
from calculator import calculate_total_average, calculate_grade, validate_score, calculate_rank
from utils import get_user_input, confirm_action

class StudentManager:
    def __init__(self):
        self.collection = db_manager.get_collection()
        
    def student_num(self):
        return get_user_input("등록할 학생 수를 입력하세요: ", int)
        
    def input_student_data(self):
        print("\n학생 정보 입력")
        student_id = get_user_input("학번: ")
        name = get_user_input("이름: ")
        
        while True:
            english = get_user_input("영어 점수: ", float)
            if validate_score(english):
                break
            print("0~100 사이의 점수를 입력하세요.")
            
        while True:
            c_language = get_user_input("C언어 점수: ", float)
            if validate_score(c_language):
                break
            print("0~100 사이의 점수를 입력하세요.")
            
        while True:
            python = get_user_input("파이썬 점수: ", float)
            if validate_score(python):
                break
            print("0~100 사이의 점수를 입력하세요.")
        
        total, average = calculate_total_average(english, c_language, python)
        grade = calculate_grade(average)
        
        return {
            'student_id': student_id,
            'name': name,
            'english': english,
            'c_language': c_language,
            'python': python,
            'total': total,
            'average': average,
            'grade': grade,
            'rank': 0
        }
    
    def add_student(self):
        try:
            student_data = self.input_student_data()
            
            # 중복 학번 체크
            if self.collection.find_one({'student_id': student_data['student_id']}):
                print("이미 존재하는 학번입니다.")
                return
            
            self.collection.insert_one(student_data)
            print("학생이 성공적으로 추가되었습니다.")
        except Exception as e:
            print(f"학생 추가 중 오류 발생: {e}")

    def delete_student(self):
        student_id = get_user_input("삭제할 학생의 학번: ")
        student = self.collection.find_one({'student_id': student_id})
        
        if not student:
            print("해당 학번의 학생을 찾을 수 없습니다.")
            return
            
        print(f"학생 정보: {student['name']} ({student['student_id']})")
        if confirm_action("정말 삭제하시겠습니까?"):
            self.collection.delete_one({'student_id': student_id})
            print("학생이 삭제되었습니다.")

    def search_student(self):
        print("1. 학번으로 검색")
        print("2. 이름으로 검색")
        choice = get_user_input("선택: ", int)
        
        if choice == 1:
            student_id = get_user_input("검색할 학번: ")
            student = self.collection.find_one({'student_id': student_id})
            if student:
                self.display_students([student])
            else:
                print("해당 학번의 학생을 찾을 수 없습니다.")
                
        elif choice == 2:
            name = get_user_input("검색할 이름: ")
            students = list(self.collection.find({'name': name}))
            if students:
                self.display_students(students)
            else:
                print("해당 이름의 학생을 찾을 수 없습니다.")

    def display_students(self, students=None):
        if students is None:
            students = list(self.collection.find())
            
        if not students:
            print("등록된 학생이 없습니다.")
            return
            
        print("\n" + "="*130)
        print(f"{'학번':<13} {'이름':<13} {'영어':<8} {'C언어':<8} {'파이썬':<8} {'총점':<8} {'평균':<6} {'학점':<6} {'등수':<7}")
        print("="*130)

        for student in students:
            print(f"{student['student_id']:<15} {student['name']:<15} "
                f"{student['english']:<10} {student['c_language']:<10} {student['python']:<10} "
                f"{student['total']:<10} {student['average']:<10} "
                f"{student['grade']:<8} {student['rank']:<8}")
        print("="*130)

    def update_ranks(self):
        students = list(self.collection.find())
        if not students:
            print("등록된 학생이 없습니다.")
            return
            
        calculate_rank(students)
        
        for student in students:
            self.collection.update_one(
                {'_id': student['_id']}, 
                {'$set': {'rank': student['rank']}}
            )
        print("등수가 업데이트되었습니다.")

    def count_above_80(self):
        count = self.collection.count_documents({'average': {'$gte': 80}})
        print(f"평균 80점 이상인 학생 수: {count}명")