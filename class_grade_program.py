 ##################
  #프로그램명: 학생점수프로그램
  #작성자: 소프트웨어학부/남유성
  #작성일: 25.04.09~25.04.12
  #프로그램 설명: Student 클래스:
  #              학번, 이름, 영어/C언어/파이썬 점수를 저장, 총점, 평균, 학점, 등수 계산 기능
  
  #            StudentManager 클래스:
  #              학생 정보 입력 (최대 5명)전체 학생 정보 출력학번/이름으로 학생 검색학생 정보 삭제총점 기준으로 학생 정렬80점 이상 학생 수 계산
  
  #            main() 함수:
  #              메뉴 출력 및 사용자 선택에 따른 기능 실행
  ###################
class Student:
    def __init__(self, student_id, name, eng, clng, python):
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.clng = clng
        self.python = python
        self.total = 0
        self.average = 0
        self.grade = ''  
        self.rank = 0
    
    def cal_total_average(self):
        self.total = self.eng + self.clng + self.python
        self.average = self.total / 3
    
    def cal_grade(self):
        if self.average >= 90:  
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else: 
            self.grade = 'F'
    
    def __str__(self):
        return f"{self.student_id}\t{self.name}\t{self.eng}\t{self.clng}\t{self.python}\t{self.total}\t{self.average:.2f}\t{self.grade}\t{self.rank}"
    
class StudentManager:  
    def __init__(self):
        self.students = []
    
    def input_student(self):
        if len(self.students) >= 5:
            print("최대 5명까지 입력 가능.")
            return
        
        student_id = input("학번: ")
        name = input("이름: ")
        
      
        for student in self.students:
            if student.student_id == student_id:
                print("이미 존재하는 학번입니다.")
                return
        
     
        try:
            english = int(input("영어 점수: "))
            clng = int(input("C언어 점수: "))
            python = int(input("Python 점수: "))
            
            if not (0 <= english <= 100 and 0 <= clng <= 100 and 0 <= python <= 100):
                print("0~100 사이의 점수를 입력하세요")
                return
                
            
            student = Student(student_id, name, english, clng, python)
            student.cal_total_average()
            student.cal_grade()
            self.students.append(student)
            self.calculate_ranks() 
            print(f"{name} 학생이 추가되었습니다.")
        except ValueError:
            print("점수는 숫자로 입력해야 합니다")
    
    def display_all_student(self):
        if not self.students:
            print("등록된 학생이 없습니다")
            return
            
        print("\n" + "-" * 70)
        print("학번\t이름\t영어점수\tC언어점수\t파이썬점수\t총점\t평균\t학점\t등수")
        print("=" * 70)
        for student in self.students:
            print(student) 
        
        high_score_count = self.over_eighty()
        print(f"\n80점 이상 학생 수: {high_score_count}")
    
    def calculate_ranks(self):  
        sorted_students = sorted(self.students, key=lambda x: x.total, reverse=True)
        for i, student in enumerate(sorted_students, 1):
            student.rank = i
    
    def search_by_id(self, student_id): 
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def search_by_name(self, name):  
        found_students = []  
        for student in self.students:
            if student.name == name:
                found_students.append(student)
        return found_students
    
    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                removed = self.students.pop(i)
                print(f"{removed.name} 학생이 삭제되었습니다")
                self.calculate_ranks()  
                return
        print("해당 학생이 존재하지 않습니다")
    
    def sort_by_total(self):  
        self.students.sort(key=lambda x: x.total, reverse=True)
        self.calculate_ranks()  
    
    def over_eighty(self):
        count = 0
        for student in self.students:  
            if student.average >= 80:
                count += 1
        return count

def main():
    manager = StudentManager() 
    
    while True:
        print("\n===== 학생 성적관리 프로그램 =====")
        print("1. 학생 정보 입력")
        print("2. 전체 학생 정보 출력")
        print("3. 학번으로 검색")
        print("4. 이름으로 검색")
        print("5. 학생 정보 삭제")
        print("6. 총점 기준 정렬")
        print("7. 80점 이상 학생 수 출력")
        print("0. 종료")
        
        choice = input("\n번호 입력: ")
        
        if choice == '1':
            manager.input_student()
        
        elif choice == '2':
            manager.display_all_student()
        
        elif choice == '3':
            student_id = input("검색할 학번: ")
            student = manager.search_by_id(student_id)  
            if student:
                print("\n" + "-" * 70)
                print("학번\t이름\t영어점수\tC언어점수\t파이썬점수\t총점\t평균\t학점\t등수")
                print("=" * 70)
                print(student)
            else:
                print("해당 학번의 학생이 존재하지 않습니다.")
        
        elif choice == '4':
            name = input("검색할 이름: ")
            students = manager.search_by_name(name)  
            if students:
                print("\n" + "-" * 70)
                print("학번\t이름\t영어점수\tC언어점수\t파이썬점수\t총점\t평균\t학점\t등수")
                print("=" * 70)
                for student in students:
                    print(student)
            else:
                print("해당 이름의 학생이 존재하지 않습니다.")
        
        elif choice == '5':
            student_id = input("삭제할 학번: ")  
            manager.delete_student(student_id)
        
        elif choice == '6':
            manager.sort_by_total()  
            print("총점 기준으로 정렬되었습니다.")
            manager.display_all_student()
        
        elif choice == '7':
            count = manager.over_eighty()
            print(f"80점 이상 학생 수: {count}명")
        
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("\n올바른 값을 입력하세요")

if __name__ == "__main__":
    main()
                    
                    
                    
                    
                    
                    
                    
                    
            
                    
            
                    
            
            
            
            
        

            
        
