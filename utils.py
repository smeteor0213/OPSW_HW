import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def print_menu():
    print("\n학생 성적 관리 시스템")
    print("-" * 30)
    print("1. 학생 추가")
    print("2. 학생 삭제") 
    print("3. 학생 검색")
    print("4. 전체 학생 조회")
    print("5. 등수 업데이트")
    print("6. 80점 이상 학생 수")
    print("0. 프로그램 종료")
    print("-" * 30)

def get_user_input(prompt, input_type=str):
    while True:
        try:
            user_input = input(prompt)
            if input_type == int:
                return int(user_input)
            elif input_type == float:
                return float(user_input)
            else:
                return user_input
        except ValueError:
            print("올바른 형식으로 입력해주세요.")

def confirm_action(message):
    while True:
        choice = input(f"{message} (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("y 또는 n을 입력해주세요.")