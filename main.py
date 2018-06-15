import os,random

from lock import lock_file
from unlock import unlock_file
from Search import search

def random_key():
    rand = random.randrange(100)
    print("{0}를 입력해 주세요.".format(rand))
    try:
        choice = int(input(">>> "), 10)
        if choice < 0 or choice > 100:
            raise ValueError
        if choice == rand:
            print("올바르게 입력하셨습니다.")
            return 1
    except ValueError:                              # 잘못된 값에 대한 예외 처리
        print("잘못된 값을 입력하셨습니다.")
        return 0

if __name__ == "__main__":
    while True:
        print("1. 파일 잠금")
        print("2. 파일 잠금 해제")
        print("3. 파일 확인")
        try:
            choice = int(input(">>> "),10)
            if choice<1 or choice >3:
                raise ValueError
        except ValueError:                          #잘못된 값에 대한 예외 처리
            print("잘못된 값을 입력하셨습니다.")
            continue
        if choice == 1:
            if random_key() == 1:
                print("잠금하고 싶은 파일의 경로를 입력해주세요.")
                path = input(">>> ")
                if not os.path.exists(path):
                    print("파일을 찾을 수 없습니다.")
                    continue

                print("잠금할 파일의 비밀번호를 입력해주세요.")
                password = input(">>> ")
                password = bytes(password, encoding='utf-8')
                lock_file(password,path)
                print("파일이 잠금이 성공적으로 되었습니다.")
            else:
                continue
        elif choice == 2:
            if random_key() == 1:
                print("잠금 해제하고 싶은 파일의 경로를 입력해주세요.")
                path = input(">>> ")
                path += ".enc"
                if not os.path.exists(path):
                    print("파일을 찾을 수 없습니다.")
                    continue

                print("잠금할 파일의 비밀번호를 입력해주세요.")
                password = input(">>> ")
                password = bytes(password,encoding='utf-8')
                if unlock_file(password, path) == 0:
                    print("비밀번호가 틀렸습니다.")
                    continue
                else:
                    print("파일 잠금 해제가 성공적으로 되었습니다.")
            else:
                continue
        elif choice == 3:
            default_path = os.path.dirname(os.path.realpath(__file__))
            file = search(default_path)
            print("프로그램이 위치한 폴더의 모든 파일 내역입니다.\n")
            for i in file:
                print(i)
            print("")