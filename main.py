from student_manager import StudentManager
from utils import print_menu, clear_screen, get_user_input, print_header
from database import db_manager

def main():
    sm = StudentManager()
    
    while True:
        clear_screen()
        print_header("학생 성적 관리 시스템")
        print_menu()
        
        try:
            choice = get_user_input("메뉴를 선택하세요: ", int)
            
            if choice == 1:
                num_students = sm.student_num()
                for i in range(num_students):
                    print(f"\n{i+1}번째 학생")
                    sm.add_student()
                    
            elif choice == 2:
                sm.delete_student()
                
            elif choice == 3:
                sm.search_student()
                
            elif choice == 4:
                sm.display_students()
                
            elif choice == 5:
                sm.update_ranks()
                
            elif choice == 6:
                sm.count_above_80()
                
            elif choice == 0:
                print("프로그램을 종료합니다.")
                break
                
            else:
                print("잘못된 메뉴입니다.")
                
        except Exception as e:
            print(f"오류 발생: {e}")
            
        if choice != 0:
            input("\n계속하려면 Enter를 누르세요...")
    
    db_manager.close_connection()

if __name__ == "__main__":
    main()