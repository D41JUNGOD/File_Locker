import os,random,time

from lock import lock_file
from unlock import unlock_file
from Search import search

def main_print():
    print(""" 
     ________  __  __                  __                            __                           
    /        |/  |/  |                /  |                          /  |                          
    $$$$$$$$/ $$/ $$ |  ______        $$ |        ______    _______ $$ |   __   ______    ______  
    $$ |__    /  |$$ | /      \       $$ |       /      \  /       |$$ |  /  | /      \  /      \ 
    $$    |   $$ |$$ |/$$$$$$  |      $$ |      /$$$$$$  |/$$$$$$$/ $$ |_/$$/ /$$$$$$  |/$$$$$$  |
    $$$$$/    $$ |$$ |$$    $$ |      $$ |      $$ |  $$ |$$ |      $$   $$<  $$    $$ |$$ |  $$/ 
    $$ |      $$ |$$ |$$$$$$$$/       $$ |_____ $$ \__$$ |$$ \_____ $$$$$$  \ $$$$$$$$/ $$ |      
    $$ |      $$ |$$ |$$       |      $$       |$$    $$/ $$       |$$ | $$  |$$       |$$ |      
    $$/       $$/ $$/  $$$$$$$/       $$$$$$$$/  $$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/ $$/                                                                                            
        """)

def lock_print():
    print(""" 
 __                            __       
/  |                          /  |      
$$ |        ______    _______ $$ |   __ 
$$ |       /      \  /       |$$ |  /  |
$$ |      /$$$$$$  |/$$$$$$$/ $$ |_/$$/ 
$$ |      $$ |  $$ |$$ |      $$   $$<  
$$ |_____ $$ \__$$ |$$ \_____ $$$$$$  \ 
$$       |$$    $$/ $$       |$$ | $$  |
$$$$$$$$/  $$$$$$/   $$$$$$$/ $$/   $$/ 
    """)

def unlock_print():
    print("""
 __    __            __                            __       
/  |  /  |          /  |                          /  |      
$$ |  $$ | _______  $$ |        ______    _______ $$ |   __ 
$$ |  $$ |/       \ $$ |       /      \  /       |$$ |  /  |
$$ |  $$ |$$$$$$$  |$$ |      /$$$$$$  |/$$$$$$$/ $$ |_/$$/ 
$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |      $$   $$<  
$$ \__$$ |$$ |  $$ |$$ |_____ $$ \__$$ |$$ \_____ $$$$$$  \ 
$$    $$/ $$ |  $$ |$$       |$$    $$/ $$       |$$ | $$  |
 $$$$$$/  $$/   $$/ $$$$$$$$/  $$$$$$/   $$$$$$$/ $$/   $$/
    """)

def usage_print():
    print(""" 
 __    __                                         
/  |  /  |                                        
$$ |  $$ |  _______   ______    ______    ______  
$$ |  $$ | /       | /      \  /      \  /      \ 
$$ |  $$ |/$$$$$$$/  $$$$$$  |/$$$$$$  |/$$$$$$  |
$$ |  $$ |$$      \  /    $$ |$$ |  $$ |$$    $$ |
$$ \__$$ | $$$$$$  |/$$$$$$$ |$$ \__$$ |$$$$$$$$/ 
$$    $$/ /     $$/ $$    $$ |$$    $$ |$$       |
 $$$$$$/  $$$$$$$/   $$$$$$$/  $$$$$$$ | $$$$$$$/ 
                              /  \__$$ |          
                              $$    $$/           
                               $$$$$$/ 
    """)

def all_file_print():
    print("""
  ______   __  __        ________  ______  __           
 /      \ /  |/  |      /        |/      |/  |          
/$$$$$$  |$$ |$$ |      $$$$$$$$/ $$$$$$/ $$ |  ______  
$$ |__$$ |$$ |$$ |      $$ |__      $$ |  $$ | /      \ 
$$    $$ |$$ |$$ |      $$    |     $$ |  $$ |/$$$$$$  |
$$$$$$$$ |$$ |$$ |      $$$$$/      $$ |  $$ |$$    $$ |
$$ |  $$ |$$ |$$ |      $$ |       _$$ |_ $$ |$$$$$$$$/ 
$$ |  $$ |$$ |$$ |      $$ |      / $$   |$$ |$$       |
$$/   $$/ $$/ $$/       $$/       $$$$$$/ $$/  $$$$$$$/
    """)

def check_print():
    print("""  
  ______   __                            __       
 /      \ /  |                          /  |      
/$$$$$$  |$$ |____    ______    _______ $$ |   __ 
$$ |  $$/ $$      \  /      \  /       |$$ |  /  |
$$ |      $$$$$$$  |/$$$$$$  |/$$$$$$$/ $$ |_/$$/ 
$$ |   __ $$ |  $$ |$$    $$ |$$ |      $$   $$<  
$$ \__/  |$$ |  $$ |$$$$$$$$/ $$ \_____ $$$$$$  \ 
$$    $$/ $$ |  $$ |$$       |$$       |$$ | $$  |
 $$$$$$/  $$/   $$/  $$$$$$$/  $$$$$$$/ $$/   $$/
    """)

def random_key():
    rand = random.randrange(100)
    print("{0}을/를 입력해 주세요.".format(rand))
    try:
        choice = int(input(">>> "), 10)
        if choice < 0 or choice > 100:
            raise ValueError

        if choice == rand:
            print("올바르게 입력하셨습니다.\n")
            return 1

    except ValueError:                              # 숫자가 아닌 값에 대한 예외 처리
        print("잘못 입력하셨습니다.\n")
        return 0

if __name__ == "__main__":
    main_print()
    while True:
        print("1. 파일 잠금")
        print("2. 파일 잠금 해제")
        print("3. 파일 찾기")
        print("4. 파일 정보 확인")
        print("5. 사용법")
        try:
            choice = int(input(">>> "),10)
            if choice<1 or choice >5:
                raise ValueError
        except ValueError:                                      #숫자가 아닌 값에 대한 예외 처리
            print("잘못 입력하셨습니다.")
            time.sleep(0.3)
            continue

        if choice == 1:
            if random_key() == 1:
                lock_print()
                print("잠금하고 싶은 파일의 경로를 입력해주세요.")
                path = input(">>> ")
                if not os.path.isfile(path):
                    print("폴더는 잠금이 불가능합니다!\n")
                    time.sleep(0.3)
                    continue

                if not os.path.exists(path):
                    print("파일을 찾을 수 없습니다.\n")
                    time.sleep(0.3)
                    continue

                print("잠금할 파일의 비밀번호를 입력해주세요.")
                password = input(">>> ")
                password = bytes(password, encoding='utf-8')
                lock_file(password,path)
                print("파일이 잠금이 성공적으로 되었습니다.\n")
                time.sleep(0.3)

            else:
                time.sleep(0.3)
                continue

        elif choice == 2:
            if random_key() == 1:
                unlock_print()
                print("잠금 해제하고 싶은 파일의 경로를 입력해주세요.")
                path = input(">>> ")
                if not os.path.isfile(path):
                    print("폴더는 잠금 해제가 불가능합니다!\n")
                    time.sleep(0.3)
                    continue

                if not os.path.exists(path):
                    print("파일을 찾을 수 없습니다.\n")
                    time.sleep(0.3)
                    continue

                print("잠금할 파일의 비밀번호를 입력해주세요.")
                password = input(">>> ")
                password = bytes(password,encoding='utf-8')
                if unlock_file(password, path) == 0:
                    print("비밀번호가 틀렸습니다.\n")
                    time.sleep(0.3)
                    continue

                else:
                    print("파일 잠금 해제가 성공적으로 되었습니다.\n")
                    time.sleep(0.3)

            else:
                time.sleep(0.3)
                continue

        elif choice == 3:
            all_file_print()
            default_path = os.path.dirname(os.path.realpath(__file__))
            file = search(default_path)
            print("프로그램이 위치한 폴더의 모든 파일 내역입니다.\n")
            for i in file:
                print(i)
            print("")

        elif choice == 4:
            check_print()
            print("확인하고 싶은 파일또는 폴더의 경로를 입력해주세요.")
            path = input(">>> ")
            if not os.path.exists(path):
                print("파일을 찾을 수 없습니다.\n")
                continue

            if os.path.isfile(path):                            #파일이라면
                extension = os.path.splitext(path)[1][1:]
                print("파일 이름 : ",os.path.basename(path))
                print("확장자 : ",extension)
                print("최근 접근 시간 : ", time.ctime(os.path.getatime(path)))
                print("최근 수정한 시간: ", time.ctime(os.path.getmtime(path)))
                print("생성시간 : ", time.ctime(os.path.getctime(path)))
                print("크기 : {0} Bytes".format(os.path.getsize(path)))
                print("")

            else:                                               #폴더라면
                print("폴더 이름 : ", os.path.basename(path))
                print("최근 접근 시간 : ", time.ctime(os.path.getatime(path)))
                print("최근 수정한 시간: ", time.ctime(os.path.getmtime(path)))
                print("생성시간 : ", time.ctime(os.path.getctime(path)))
                print("크기 : {0} Bytes".format(os.path.getsize(path)))
                print("")

        elif choice == 5:
            usage_print()
            print("파일 잠금 - 비밀번호를 입력하고 파일을 잠급니다.\n")
            print("파일 잠금 해제 - 비밀번호를 입력하고 파일 잠금을 해제합니다.\n")
            print("파일 찾기 - 프로그램이 위치한 폴더의 모든 파일들을 보여줍니다.\n")
            print("파일 정보 확인 - 파일 또는 폴더의 파일 속성 정보들을 보여줍니다.\n")


