#  application/run.py
# 만들어진 서버 객체를 실행한다.

from create import create_app # create.py에 create_app 함수를 import

app = create_app()

if __name__ == '__main__':
    app.run() #cerate_app에서 DEBUG = True해놔서 여기서 별도로 설정해주지 않아도 된다.


# 서버를 run 한 다음 켜졌는지 확인하는 방법은
# 1. 직접접속, 2. curl로 날리기, 3. postman 등 요청 (그냥 http요청 해보는 것들 ㅇㅇ)