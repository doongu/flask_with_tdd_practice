# tdd_practice
## API tdd_practice_example
개발하고자 하는 프로젝트 서버의 API 테스트를 위한 코드입니다.
### 어떤 필요한 데이터들을 생성해서 test를 해볼 것인가?를 주된 관점으로 작성해보았습니다.
### 서버에 대한 API 요청을 테스트 해볼 것이기에, 이에 필요한 요소들을 정리해보겠습니다.
******************
1. 파라메타 (GET, POST, PUT, DELETE 4개)
2. uri 에서 url을 뺀 부분 ( path 부분 )
4. port 번호
3. 2번에서 추출한 값을 http://localhost:포트번호/path 로 지정하고, 이 uri들을 저장
5. 3번에서 저장한 값을 GET, POST, PUT, DELETE에 맞게 요청이 올바른지 에 대한 TDD 진행

ex) http://localhost:80/main 으로 POST요청이 들어온 것은 200error 외에는 전부 400 Bad Request로 처리.
******************




# DB tdd_practice_example




## API tdd_practice_example
TDD 예제 및 연습 해보기 위한 repository입니다.
저는 프로젝트 개발을 여러가지 해보았지만, 그간 혼자 개발을 해와서 그랬는지 구체적인 틀이나 패턴을 참고하여 프로젝트를 진행해본적이 없습니다. 그래서 TDD와 패턴을 공부하고자 하는 flask app repository입니다.
연습은 https://medium.com/@homekeeper89/flask-with-tdd-chapter-1-%EC%84%9C%EB%B2%84%EC%84%A4%EC%A0%95-a587f33c3311
를 토대로 연습합니다.

fake data 참조
https://www.daleseo.com/python-faker/
https://github.com/iml1111/IMFlask-Pymongo/blob/main/IMFlask/tests/mock.py

mock 참조 
https://www.daleseo.com/python-unittest-mock-patch/#patching-mocking
